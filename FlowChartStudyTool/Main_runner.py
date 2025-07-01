# main.py

class TreeNode:
    """
    A class to represent a single node in a binary tree.
    Each node holds a piece of data (a question or a final answer)
    and has pointers to a left child ('no' branch) and a right child ('yes' branch).
    """
    def __init__(self, data):
        self.data = data
        self.left = None  # Represents the 'No' path
        self.right = None # Represents the 'Yes' path

def get_user_choice(prompt):
    """
    A helper function to get a validated choice from the user.
    Loops until the user enters a valid option.
    """
    while True:
        choice = input(prompt).lower().strip()
        if choice in ['y', 'n', 'yes', 'no']:
            return choice == 'y' or choice == 'yes'
        elif choice in ['q', 'l', 'question', 'leaf']:
            return choice
        else:
            print("Invalid input. Please try again.")

def build_tree():
    """
    Recursively builds a binary tree based on user input.
    This function constructs a single node and then calls itself to build
    the 'no' and 'yes' sub-trees.
    """
    # Get the data for the current node (either a question or a leaf answer)
    node_data = input("Enter the text for this node (question or final answer): ").strip()
    current_node = TreeNode(node_data)

    # Ask if this node should be a leaf (have no further questions)
    is_leaf = get_user_choice("Is this a leaf node (a final answer)? (y/n): ")
    if is_leaf:
        return current_node # This branch of the tree is complete

    # --- Build the 'No' (left) branch ---
    print(f"\nLet's define the 'NO' branch for the question: '{node_data}'")
    current_node.left = build_tree()

    # --- Build the 'Yes' (right) branch ---
    print(f"\nLet's define the 'YES' branch for the question: '{node_data}'")
    current_node.right = build_tree()

    return current_node

def take_quiz(root_node):
    """
    Traverses the binary tree from the root based on user's yes/no answers.
    Starts at the root and moves down until a leaf node is reached.
    """
    if not root_node:
        print("The tree is empty! Please build a tree first.")
        return

    current_node = root_node
    print("\n--- Starting Quiz ---")
    print("Answer the following questions with 'yes' or 'no'.")

    # Loop until we reach a leaf node (a node with no children)
    while current_node.left is not None and current_node.right is not None:
        is_yes = get_user_choice(f"Question: {current_node.data} (yes/no): ")
        
        if is_yes:
            current_node = current_node.right
        else:
            current_node = current_node.left

    # When the loop finishes, we are at a leaf node.
    print("\n--- Result ---")
    print(f"Conclusion: {current_node.data}")
    print("----------------")


def main():
    """
    The main function to run the study tool.
    It orchestrates the building of the tree and the quizzing loop.
    """
    print("--- Binary Tree Study Tool ---")
    print("First, let's build your study tree.")
    print("You will define questions and the 'yes'/'no' paths for each.")
    
    # Build the entire tree, starting from the root.
    root = build_tree()
    
    print("\n********************************")
    print("Tree construction complete!")
    print("********************************")

    # Allow the user to take the quiz multiple times
    while True:
        take_quiz(root)
        
        play_again = get_user_choice("\nWould you like to take the quiz again? (y/n): ")
        if not play_again:
            break
            
    print("\nThank you for using the Study Tool. Goodbye!")


if __name__ == "__main__":
    main()
