"""An optimized implementation of Suffix-Tree."""

# For more infor about the comments you can read http://web.stanford.edu/~mjkay/gusfield.pdf
import sys
from operator import attrgetter

leafEnd = -1


# https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/
# Idea based on c++ code from geek
class Node:
    """Node of Suffix-Tree"""

    def __init__(self, leaf):
        # children of this node
        self.children = {}
        # True if having a leaf, False if no
        self.leaf = leaf
        # This leaf node contains the suffix index for the route from root to leaf.
        self.suffix_index = None
        """(start, end) interval specifies the edge, by which the
            node is connected to its parent node. Each edge will
            connect two nodes, one parent and one child, and
            (start, end) interval of a given edge will be stored
            in the child node. Lets say there are two nods A and B
            connected by an edge with indices (5, 8) then this
            indices (5, 8) will be stored in node B. """
        self.start = None
        self.end = None
        # pointer to other node via suffix link
        self.suffix_link = None

    def __getattribute__(self, name):
        if name == 'end':
            if self.leaf:
                return leafEnd
        # Calling the super class to avoid recursion
        return super(Node, self).__getattribute__(name)


class SuffixTree:
    """The Suffix-Tree."""

    def __init__(self, text):
        """Initiate the tree."""
        self.text_string = text
        self.size = -1  # Length of input string
        self.root = None
        """last_new_node will point to newly created internal node,
        waiting for it's suffix link to be set, which might get
        a new suffix link (other than root) in next extension of
        same phase. last_new_node will be set to NULL when last
        newly created internal node (if there is any) got it's
        suffix link reset to new internal node created in next
        extension of same phase. """
        self.last_new_node = None
        self.active_node = None
        """active_edge is represented as input string character
          index (not the character itself)"""
        self.active_edge = -1
        self.active_length = 0
        # remainder_suffix_count tells how many suffixes yet to
        # be added in tree
        self.remainder_suffix_count = 0
        self.root_end = None
        self.split_end = None

    def edge_length(self, node):
        if node == self.root:
            return 0
        return node.end - node.start + 1

    def skip_counting(self, current_node):
        """skip_counting from current node.
        activePoint change for walk down (APCFWD) using
        Skip/Count Trick  (Trick 1). If active_length is greater
        than current edge length, set next  internal node as
        active_node and adjust active_edge and active_length
        accordingly to represent same activePoint.
        """
        length = self.edge_length(current_node)
        if self.active_length >= length:
            self.active_edge += length
            self.active_length -= length
            self.active_node = current_node
            return True
        return False

    def create_a_new_node(self, start, end=None, leaf=False):
        """For root node, suffix_link will be set to NULL
        For internal nodes, suffix_link will be set to root
        by default in  current extension and may change in
        next extension"""
        node = Node(leaf)
        node.suffix_link = self.root
        node.start = start
        node.end = end
        """suffix_index will be set to -1 by default and
           actual suffix index will be set later for leaves
           at the end of all phases"""
        node.suffix_index = -1
        return node

    def extend_suffix_tree(self, pos):

        global leafEnd
        """Extension Rule 1, this takes care of extending all
        leaves created so far in tree"""
        leafEnd = pos
        """Increment remainder_suffix_count indicating that a
        new suffix added to the list of suffixes yet to be
        added in tree"""
        self.remainder_suffix_count += 1
        """set last_new_node to None while starting a new phase,
         indicating there is no internal node waiting for
         it's suffix link reset in current phase"""
        self.last_new_node = None
        # Add all suffixes (yet to be added) one by one in tree
        while self.remainder_suffix_count > 0:
            if self.active_length == 0:
                self.active_edge = pos  # APCFALZ
            #  There is no outgoing edge starting with
            #  active_edge from active_node
            if self.active_node.children.get(self.text_string[self.active_edge]) is None:
                # Extension Rule 2 (A new leaf edge gets created)

                self.active_node.children[self.text_string[self.active_edge]] = self.create_a_new_node(pos, leaf=True)
                """A new leaf edge is created in above line starting
                 from  an existng node (the current active_node), and
                 if there is any internal node waiting for it's suffix
                 link get reset, point the suffix link from that last
                     internal node to current active_node. Then set last_new_node
                 to None indicating no more node waiting for suffix link
                 reset."""
                if self.last_new_node is not None:
                    self.last_new_node.suffix_link = self.active_node
                    self.last_new_node = None
            #  There is an outgoing edge starting with active_edge
            #  from active_node
            else:
                #  Get the next node at the end of edge starting
                #  with active_edge
                next_node = self.active_node.children.get(self.text_string[self.active_edge])
                if self.skip_counting(next_node):  # Do skip_counting
                    # Start from next_node node (the new active_node)
                    continue
                """Extension Rule 3 (current character being processed
                  is already on the edge)"""
                print("Rule 3", next_node.start + self.active_length, pos)
                if self.text_string[next_node.start + self.active_length] == self.text_string[pos]:
                    # If a newly created node waiting for it's
                    # suffix link to be set, then set suffix link
                    # of that waiting node to curent. active node
                    if (self.last_new_node is not None) and (self.active_node != self.root):
                        self.last_new_node.suffix_link = self.active_node
                        self.last_new_node = None
                    # APCFER3
                    self.active_length += 1
                    """STOP all further processing in this phase
                    and move on to next_node phase"""
                    break
                """We will be here when activePoint is in middle of
                  the edge being traversed and current character
                  being processed is not  on the edge (we fall off
                  the tree). In this case, we add a new internal node
                  and a new leaf edge going out of that new node. This
                  is Extension Rule 2, where a new leaf edge and a new
                internal node get created"""
                self.split_end = next_node.start + self.active_length - 1
                # New internal node
                split = self.create_a_new_node(next_node.start, self.split_end)
                self.active_node.children[self.text_string[self.active_edge]] = split
                # New leaf coming out of new internal node
                split.children[self.text_string[pos]] = self.create_a_new_node(pos, leaf=True)
                next_node.start += self.active_length
                split.children[self.text_string[next_node.start]] = next_node
                """We got a new internal node here. If there is any
                  internal node created in last extensions of same
                  phase which is still waiting for it's suffix link
                  reset, do it now."""
                if self.last_new_node is not None:
                    # suffix_link of last_new_node points to current newly
                    # created internal node
                    self.last_new_node.suffix_link = split
                """Make the current newly created internal node waiting
                  for it's suffix link reset (which is pointing to self.root
                  at present). If we come across any other internal node
                  (existing or newly created) in next extension of same
                  phase, when a new leaf edge gets added (i.e. when
                  Extension Rule 2 applies is any of the next extension
                  of same phase) at that point, suffix_link of this node
                  will point to that internal node."""
                self.last_new_node = split
            """One suffix got added in tree, decrement the count of
               suffixes yet to be added."""
            self.remainder_suffix_count -= 1
            if (self.active_node == self.root) and (self.active_length > 0):  # APCFER2C1
                self.active_length -= 1
                self.active_edge = pos - self.remainder_suffix_count + 1
            elif self.active_node != self.root:  # APCFER2C2
                self.active_node = self.active_node.suffix_link


    def build_suffix_tree(self):
        self.size = len(self.text_string)

        """Root is a special node with start and end indices as -1,
        as it has no parent from where an edge comes to root"""
        self.root_end = -1
        self.root = self.create_a_new_node(-1, self.root_end)
        self.active_node = self.root  # First active_node will be root
        for i in range(self.size):
            self.extend_suffix_tree(i)
        self.set_suffix_index(self.root, 0)

    """
       When we build successful the suffix tree, i will use dfs to travel to the end node in each branch. 
       However, in each move I will choose to go in ascending order of characters from the ASCII range [10, 126]. 
       When we reach the endpoint with the value len(string), we need to know where the character from the root node is 
       located on the string. For example, "abacabad$"(0,1,2,3,4,5,6,7,8), from root it has a branch containing "three",
        then it has 2 branches "d$" and "cabad$". How do I return (5,8) for "bad$", and (1,8) for "bacabad$". 
        I will have a variable lo_start so that I can add up the length of one branch, before jumping to another branch
        I will update lo_start += end + 1 - start. Then when I get to the branch containing the end node, I simply subtract 
        the lo_start from the starting position of that branch. After I have the result of that branch, because I move in
         ascending order and I use the result of pre_cal and apply the value I earn of each end branch. I will get the 
         corresponding burrow wheeler transform.
       """

    def set_suffix_index(self, current, lo_start):

        start, end = current.start, current.end

        if len(current.children) == 0:
            current.suffix_index = start - lo_start

        for i in range(0, 256):
            ch = chr(i)

            if ch not in current.children:
                continue
            node = current.children[ch]
            if node:
                temp = 0
                if start != -1:
                    temp = lo_start + self.edge_length(current)
                self.set_suffix_index(node, temp)

    # check the pattern match the orginal text or not
    def check(self, pat, idx, start, end):

        for i in range(start, end + 1):
            if self.text_string[i] == '$':
                break
            if idx == len(pat):  # 2 string match
                return 1
            if pat[idx] == '?':
                idx += 1
                continue
            if self.text_string[i] != pat[idx]:
                return -1  # no match
            idx += 1
            if idx == len(pat):  # 2 string match
                return 1
        if idx == len(pat):  # 2 string match
            return 1
        return 0  # more characters to match pat and text_string

    """
    When a suffix tree is built, from a point we can travel to repeat points with it that will 
    start in the same branch with the same parent.
    """

    def found_position_match(self, current):
        global pos
        if current is None:
            return
        if current.suffix_index > -1:
            pos.append(current.suffix_index)
            return

        for i in range(10, 127):
            ch = chr(i)
            if ch not in current.children:
                continue
            # find the all next child branches
            self.found_position_match(current.children[ch])
        return

    def dfs_tree(self, current, pat, idx):
        global pos
        if current is None:
            return
        # if current is not root node, then traverse edge
        # from node n's parent to node n.
        if current.start != -1:
            res = self.check(pat, idx, current.start, current.end)  # check the pattern match the orginal text or not
            print(res)
            if res == -1:  # if not return
                return
            if res == 1:  # match 2 strings
                # more characters to match pat and text_string.
                if current.suffix_index > -1:
                    pos.append(current.suffix_index)
                else:
                    """
                    Start from root node so current.suffix_index always is -1
                    If we come from this node, and check that it matches the pattern, then we will traverse the
                     sub-branches that develop from this node and which node has suffix index >-1, indicating pattern matching
                    """

                    self.found_position_match(current)
                return
        # Get the character index to search
        idx += self.edge_length(current)

        if idx >= len(pat):
            return
        """
        If there is an edge from node n going out
        with current character str[idx], traverse that edge
        """
        if pat[idx] not in current.children and pat[idx] != '?':
            return
        if pat[idx] == '?':
            for i in range(10, 127):
                ch = chr(i)
                if ch not in current.children:
                    continue
                print(ch)
                self.dfs_tree(current.children[ch], pat, idx)
        else:
            self.dfs_tree(current.children[pat[idx]], pat, idx)


def readInput(txtFileName, patFileName):
    # Open and read the text file
    txtFile = open(txtFileName, 'r')
    txt = txtFile.read()
    # Remember to close the file
    txtFile.close()
    # Open and read the pattern file
    patFile = open(patFileName, 'r')
    pat = patFile.read()
    # Remember to close the file
    patFile.close()

    return txt, pat


def writeOutput(occurrences):
    # Open output file with correct name
    outputFile = open('output_wildcard_matching.txt', 'w')
    # Iterate through the occurrence list and write results to an output file

    for i in range(0, len(occurrences)):
        outputFile.write(str(occurrences[i] + 1))
        outputFile.write('\n')
    # Remember to close the file
    outputFile.close()


if __name__ == '__main__':
    global pos
    pos = []
    txtFileName = sys.argv[1]
    patFileName = sys.argv[2]
    txt, pat = readInput(txtFileName, patFileName)
    txt += '$'
    a = SuffixTree(txt)
    a.build_suffix_tree()
    a.dfs_tree(a.root, pat, 0)
    pos.sort()
    writeOutput(pos)
