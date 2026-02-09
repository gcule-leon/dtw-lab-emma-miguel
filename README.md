# Lab Workflow – Steps Followed

## 1. Repository Preparation
1. Cloned the professors' repository.
2. Cloned our own repository, previously configured manually.
3. Copied the `/materials` directory from the professors' repository into our repository.
4. Performed the first commit and pushed it to `main`. Since the repository was initially empty, pushing directly to `main` was allowed.

---

## 2. Python Environment Setup
5. Created the Python environment and synchronized project dependencies using the appropriate environment setup command.

---

## 3. Feature Development (Data Cleaning)
6. Created a new feature branch named `feature/clean_data` and switched to it.
7. Modified the code in this branch and pushed the changes to the remote repository.
8. Executed the application and obtained the following result:

The mean value for the charge left percentage is 33.200312292697866

---

## 4. Updating Main Branch
9. Applied a modification on the `main` branch to correctly access the cleaning function. After execution, the result changed to:

The mean value for the charge left percentage is 33.084664003107484


Additionally, outliers were successfully removed from the generated graphs.

10. Changes were pushed using the GitHub interface integrated in VS Code.

---

## 5. Pull Request and Merge Process
11. While creating the Pull Request, permission issues appeared, similar to what happened previously in class. Repository settings were updated to allow merging.
12. After approval and merge completion, all branches were fetched locally, and the updated changes from `main` were downloaded.

---

## 6. Conflict Simulation
13. To simulate merge conflicts, a new branch was created and changes were made in `main.py`. These changes were merged on GitHub through a Pull Request, but the updates were intentionally not downloaded locally so that the local repository remained outdated.

14. A new local branch was then created from the outdated version of `main`.
15. In this branch, exactly the same word was modified as in the previously merged remote change, ensuring a conflict scenario.
16. When creating a new Pull Request, GitHub detected the conflict. After resolving it and completing the merge, branches were updated locally and the commit history confirmed that merges and history matched the reference repository provided by the professors.


---

## 7. Final Functional Improvement
17. As a final step, a functional improvement was introduced: instead of computing the mean value, the application was modified to compute the median value of the charge percentage.

The final execution produced:

The mode value for the charge left PERCENTAGE is 32.31

## 8. Final Functional Change Test