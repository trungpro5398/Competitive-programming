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

        print(self.active_node.children)
        print("Active length:",self.active_length)
        print("Last new node",self.last_new_node)
        print("Rem :", self.remainder_suffix_count)
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
                print("Rule 3",next_node.start + self.active_length, pos)
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
        print()

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
    def find_the_smallest_string_by_dfs(self, current, lo_start):
        global cnt
        cnt += 1
        start, end = current.start, current.end
        print((self.text_string[start: end + 1], end - (lo_start + end - start),start, end))
        if len(current.children) == 0:
            yield start - lo_start

        for i in range(0, 256):
            ch = chr(i)

            if ch not in current.children:
                continue
            node = current.children[ch]
            if node:
                temp = 0
                if start != -1:
                    temp = lo_start + end + 1 - start
                yield from self.find_the_smallest_string_by_dfs(node, temp)

    def build_suffix_tree(self):
        self.size = len(self.text_string)

        """Root is a special node with start and end indices as -1,
        as it has no parent from where an edge comes to root"""
        self.root_end = -1
        self.root = self.create_a_new_node(-1, self.root_end)
        self.active_node = self.root  # First active_node will be root
        for i in range(self.size):
            self.extend_suffix_tree(i)

    def __str__(self):
        return "\n".join(map(str, self.edges.values()))

    def burrow_wheeler(self):
        global cnt
        cnt = 0
        res = []
        for sub in self.find_the_smallest_string_by_dfs(self.root, 0):
            res.append(sub)
        return res

"""
This method will pre calculate the first and the final in the original string, when the string rotates all
cyclic. For example, "abacabad$" (0,1,2,3,4,5,6,7,8)
abacabad$ the first string is 'a' location 0, the final string is '$' location 8
bacabad$a the first string is 'b' location 1, the final string is 'a' location 0
acabad$ab the first string is 'a' location 2, the final string is 'b' location 1
...
 
"""
def pre_cal(string):
    right = len(string) - 1
    location = [0] * len(string)
    for i in range(len(string)):
        location[i] = right
        right += 1
        if right == len(string):
            right = 0
    return location

def readInput(txtFileName):
    # Open and read the text file
    txtFile = open(txtFileName, 'r')
    txt = txtFile.read()
    # Remember to close the file
    txtFile.close()

    return txt

def writeOutput(result):
    # Open output file with correct name
    outputFile = open('output_bwt_1.txt', 'w')
    # Iterate through the occurrence list and write results to an output file
    outputFile.write(result)
    # Remember to close the file
    outputFile.close()
if __name__ == '__main__':
    txtFileName = sys.argv[1]
    txt = readInput(txtFileName,)
    a = SuffixTree(txt)
    a.build_suffix_tree()
    res = a.burrow_wheeler()
    location = pre_cal(txt)
    final_res = ""
    for i in res:
        final_res += txt[location[i]]
    writeOutput(final_res)
