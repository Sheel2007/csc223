## 1.1 Getting Started - About Version Control

### About Version Control
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. It is essential for managing changes in software source code and various types of files on a computer. Version control allows you to revert files to previous states, compare changes over time, identify contributors, and recover data in case of errors or file loss.

### Local Version Control Systems
Local Version Control Systems (VCSs) were developed to address the need for a simple way to manage file revisions locally. These systems, such as RCS, store patch sets to represent differences between files and enable users to revert files to previous states.

### Centralized Version Control Systems
Centralized Version Control Systems (CVCSs) were introduced to facilitate collaboration among developers working on different systems. In a CVCS, a central server stores all versioned files, and clients interact with the server to check out files. While CVCSs offer advantages like centralized administration and visibility into team activities, they have drawbacks such as a single point of failure and dependency on the central server for collaboration.

### Distributed Version Control Systems
Distributed Version Control Systems (DVCSs), such as Git, Mercurial, and Darcs, provide a decentralized approach to version control. In a DVCS, clients maintain a full copy of the repository, including its entire history. This enables users to collaborate without dependency on a central server and allows for easier data recovery in case of server failure. DVCSs support multiple remote repositories and diverse collaboration workflows, offering flexibility and robustness in managing project histories and collaborations.

## 1.2 Getting Started - A Short History of Git

### A Short History of Git
Git originated from the Linux kernel development community's need for a distributed version control system (DVCS) following a fallout with the proprietary DVCS, BitKeeper, in 2005.

#### Background
- The Linux kernel project initially used patch files and archived files for version control from 1991 to 2002.
- In 2002, BitKeeper, a proprietary DVCS, was adopted for Linux kernel maintenance.

#### Breakdown with BitKeeper
- In 2005, the relationship between the Linux community and BitKeeper's commercial developer deteriorated.
- BitKeeper's free-of-charge status was revoked, prompting the Linux community to seek an alternative.

#### Development of Git
- Linus Torvalds, the creator of Linux, led the development of Git as a replacement for BitKeeper.
- Key goals for Git included speed, simplicity, robust support for non-linear development, and full distribution.

#### Evolution of Git
- Git was designed to be fast, efficient with large projects like the Linux kernel, and feature-rich with a powerful branching system.

Since its inception in 2005, Git has continued to evolve and mature while retaining its initial principles, making it a widely used and highly regarded version control system.

## 1.4 Getting Started - The Command Line

### The Command Line
Git can be used through various interfaces, including command-line tools and graphical user interfaces (GUIs). However, this book focuses on using Git via the command line for several reasons:

#### Full Git Functionality
- The command line provides access to all Git commands and functionalities.
- Most GUIs offer only a subset of Git functionality for simplicity, while the command-line version allows access to the complete set of features.

#### Transferable Skills
- Knowledge of the command-line version allows users to easily transition to using GUIs if needed.
- Conversely, familiarity with GUIs does not necessarily translate to proficiency in using the command-line version.

#### Universal Availability
- Command-line tools are universally available across different systems and platforms.
- While graphical clients may vary based on personal preferences, all users can access the command-line tools without additional installations.

### Getting Started with the Command Line
To follow the examples and descriptions in this book, it's essential to be familiar with opening and using the command line in your operating system:
- On macOS, you'll need to know how to open Terminal.
- On Windows, you'll need to know how to open Command Prompt or PowerShell.

If you're not familiar with these concepts, it's recommended to pause and quickly research them to ensure you can follow along with the rest of the content in this book.
