# Binary Tree Study Tool

A simple and powerful command-line tool written in Python that allows you to create your own custom flowchart-style study guides using a binary tree structure. Build a tree of questions and then quiz yourself to reinforce your knowledge by following the "yes" or "no" paths to their logical conclusions.

This tool was inspired by studying for a flowchart quiz and realizing that a binary tree is the perfect data structure for modeling decision-based paths.

## Features

-   **Custom Tree Creation**: Interactively build your own binary decision tree from the command line.
-   **Question & Answer Nodes**: Populate each node with a question to guide the user.
-   **Yes/No Branching**: Define distinct paths for "yes" and "no" answers, creating a logical flow.
-   **Leaf Node Conclusions**: End each path in a "leaf" node, which represents the final answer or conclusion.
-   **Interactive Quiz Mode**: Once your tree is built, you can quiz yourself as many times as you like.
-   **Pure Python**: No external libraries needed! Just a standard Python installation.

## How to Use

1.  **Download the Code**: Save the code as a Python file (e.g., `study_tool.py`).
2.  **Run from Terminal**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script:
    ```bash
    python study_tool.py
    ```
3.  **Build Your Tree**: The program will first guide you through building the tree.
    -   You'll start by entering the text for the root question.
    -   For each question, you will be asked if it's a "leaf node" (a final answer). If you say `n` (no), you will then define its "No" and "Yes" branches.
    -   The process is recursive. When defining a branch, you are essentially creating a new node, which can be another question or a final leaf node.
    -   Continue this process until all branches of your logic end in a leaf node.

4.  **Take the Quiz**:
    -   Once the tree is fully constructed, the quiz will begin automatically.
    -   Answer each question with `yes` or `no` (or `y`/`n`).
    -   The tool will navigate you through the tree based on your answers until it reaches a conclusion.
    -   After the quiz is finished, you'll have the option to take it again or exit the program.

## Example Walkthrough

Let's build a simple tree to identify an animal.

**Building Phase:**

$ python study_tool.py--- Binary Tree Study Tool ---First, let's build your study tree.You will define questions and the 'yes'/'no' paths for each.Enter the text for this node (question or final answer): Does it live in the ocean?Is this a leaf node (a final answer)? (y/n): nLet's define the 'NO' branch for the question: 'Does it live in the ocean?'Enter the text for this node (question or final answer): Does it have stripes?Is this a leaf node (a final answer)? (y/n): nLet's define the 'NO' branch for the question: 'Does it have stripes?'Enter the text for this node (question or final answer): It might be a Lion.Is this a leaf node (a final answer)? (y/n): yLet's define the 'YES' branch for the question: 'Does it have stripes?'Enter the text for this node (question or final answer): It might be a Zebra.Is this a leaf node (a final answer)? (y/n): yLet's define the 'YES' branch for the question: 'Does it live in the ocean?'Enter the text for this node (question or final answer): Is it a mammal?Is this a leaf node (a final answer)? (y/n): nLet's define the 'NO' branch for the question: 'Is it a mammal?'Enter the text for this node (question or final answer): It might be a Fish.Is this a leaf node (a final answer)? (y/n): yLet's define the 'YES' branch for the question: 'Is it a mammal?'Enter the text for this node (question or final answer): It might be a Whale.Is this a leaf node (a final answer)? (y/n): yTree construction complete!
**Quizzing Phase:**

--- Starting Quiz ---Answer the following questions with 'yes' or 'no'.Question: Does it live in the ocean? (yes/no): yesQuestion: Is it a mammal? (yes/no): yes--- Result --- Conclusion: It might be a Whale.Would you like to take the quiz again? (y/n): y--- Starting Quiz ---Answer the following questions with 'yes' or 'no'.Question: Does it live in the ocean? (yes/no): noQuestion: Does it have stripes? (yes/no): yes--- Result --- Conclusion: It might be a Zebra.Would you like to take the quiz again? (y/n): nThank you for using the Study Tool. Goodbye!
## Code Overview

-   `TreeNode` **class**: The basic building block. Each instance holds `data` (text) and pointers to `left` (no) and `right` (yes) children.
-   `build_tree()`: A recursive function that prompts the user to create a node and then calls itself to build out the left and right sub-trees until a leaf is created.
-   `take_quiz(root_node)`: A function that traverses the tree by taking user input (`yes`/`no`) and moving to the appropriate child node until a leaf is reached.
-   `main()`: The main driver of the program. It initiates the tree-building process and then enters a loop for the quiz.
