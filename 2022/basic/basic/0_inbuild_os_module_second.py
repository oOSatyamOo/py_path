# Python Interview Questions on OS Modules
# What is OS Module in Python?
# How to open  an OS Module in Python?
# What is the use of OS Module in Python?
# What is OS Path Module in Python?
# What is import OS SYS in Python?

# 31 & 32 Aspect	os.mkdir	os.makedirs
# Creates Intermediate Dirs	No (raises FileNotFoundError)	Yes (creates all missing directories)
# Single vs Nested Dirs	Single directory only	Handles both single and nested dirs
# Handles Existing Dir	Raises FileExistsError	Optional (exist_ok=True avoids error)
# Use Case	Simple directory creation	Building complex directory structures


# 33. minor(device) & major(device)
# In Unix-like systems, device files are special files in the /dev directory that represent hardware devices (e.g., disks, terminals, printers). These files are associated with a device ID, which consists of two parts:

# Major Number: Identifies the type of device (e.g., disk, terminal).
# Minor Number: Identifies a specific device instance within that type (e.g., a specific disk partition).
# Use Case: Helps identify the type of device associated with the device ID.
# device: A device ID, typically retrieved using os.stat() or os.lstat() on a device file.
# import os
# # Path to a device file
# device_path = "/dev/sda"
# # Get metadata about the device file
# stat_info = os.stat(device_path)
# # Extract the major and minor device numbers
# major_number = os.major(stat_info.st_rdev)
# print("Major Number:", major_number)
# Example: 8 typically corresponds to SCSI disk devices on Linux.
# - System Administration:
# System tools or scripts can use the major number to group or categorize devices in /dev.
# - Custom Device Drivers: When creating custom device drivers, major numbers are assigned to the driver to define its device type.
# How Device IDs Work
# Device IDs are stored in a special attribute of a file's metadata called st_rdev. You can retrieve it using os.stat() or os.lstat().

# Example of Device ID Decomposition
# import os
# # Path to a device file
# device_path = "/dev/sda"
# # Get metadata about the device file
# stat_info = os.stat(device_path)
# # Extract major and minor numbers
# major_number = os.major(stat_info.st_rdev)
# minor_number = os.minor(stat_info.st_rdev)
# print("Device ID:", stat_info.st_rdev)
# print("Major Number:", major_number)
# print("Minor Number:", minor_number)
# Output (example):
# Device ID: 2048
# Major Number: 8
# Minor Number: 0
# Here:
# Major Number 8: Represents a block storage device (SCSI disk).
# Minor Number 0: Represents the first disk (/dev/sda).

# List of Major Device Numbers by Category
# 1. Block Devices (Storage)
# Block devices are devices that store data in fixed-size blocks (e.g., disks).
# Device	Major Number	Description
# SCSI Disk Drives	8	For devices like /dev/sda, /dev/sdb (hard drives).
# IDE Disk Drives	3	Legacy IDE hard drives (/dev/hda, /dev/hdb).
# NVMe Drives	259	Modern NVMe storage devices.
# Loopback Devices	7	Virtual block devices (/dev/loop0, /dev/loop1).
# RAM Disk	1	In-memory block devices (/dev/ram0).
# USB Mass Storage	189	USB drives (external storage).



# 35. mkfifo(path[, mode])
# where mkdir() default is 0o777(0777) and mkfifo default octal is 0o600(0666).
# It create a FIFO (First In, First Out) special file, also known as a named pipe, at the specified path. Named pipes enable interprocess communication (IPC) by allowing data to be written by one process and read by another, working like a queue.

# >>> path = "/tmp/hourly"
# >>> os.mkfifo( path, 0644 )
# The os.mkfifo(path[, mode]) function in Python is used to create a FIFO (First In, First Out) special file, also known as a named pipe, at the specified path. Named pipes enable interprocess communication (IPC) by allowing data to be written by one process and read by another, working like a queue.
# Real-World Use Cases of os.mkfifo
# Interprocess Communication (IPC):
# Named pipes allow two or more processes to communicate by passing data in a producer-consumer model. For example:
# Producer process writes data to the named pipe.
# Consumer process reads data from the named pipe.
# This is useful when processes need to share data without relying on intermediate files.
# Logging and Monitoring:
# A process can continuously write logs to a named pipe, while another process reads and monitors the logs in real time.
# This avoids the overhead of writing logs to a physical file.
# Stream Processing:
# A producer can stream data (e.g., video, audio, or text) through a named pipe, and a consumer can process it (e.g., encode, analyze, or display) in real time.
# Simulating File Input for Programs:
# A named pipe can be used to simulate a file for programs that expect file input but should instead process dynamically generated data.
# Decoupling of Processes:
# Using a named pipe allows decoupling of two processes so they can work independently, as long as they adhere to the FIFO read/write behavior.

# Key Points:
# Blocking Behavior:
# Reading from a named pipe blocks until data is available.
# Writing to a named pipe blocks until a reader is available.
# This behavior ensures synchronization between producer and consumer processes.
# Permissions:
# The mode parameter controls who can read/write to the pipe.
# Example: 0o600 allows only the owner to read and write.
# System-Specific:
# Named pipes work on Unix-like systems (Linux, macOS). On Windows, consider using the subprocess module or Windows-specific IPC mechanisms for similar functionality.
# Named vs. Anonymous Pipes:
# Named pipes (via os.mkfifo) exist as a file in the filesystem and can be accessed by multiple unrelated processes.
# Anonymous pipes are created on-the-fly and used only between related processes (e.g., parent and child).

# 36 mknod(filename[, mode=0600, device]) as a way to create special files in a computer's storage system. These files are not just 
# regular documents like Word files or images—they are "special" because they serve unique purposes, such as acting as communication
# tools or helpers for the operating system.
# This Python os Module will create a filesystem node named ‘filename’. This can be a file, a device-special file, or a named pipe.
# Imagine This:
# You’re organizing a large event. You need different tools for different tasks:
# A regular notepad for taking notes (this is like a regular file).
# A tube where one person can send messages to another person (this is like a named pipe).
# A control panel for managing devices like lights or speakers (this is like a device file).

# >>> filename = '/tmp/tmpfile'
# >>> mode = 0600|stat.S_IRUSR
# >>> os.mknod(filename, mode)
#  create special files in a computer's storage system. These files are not just regular documents
# like Word files or images—they are "special" because they serve unique purposes, such as 
# acting as communication tools or helpers for the operating system.


# 37. open(file, flags[, mode])
# The flags may take one of these values, or a bitwise-OR combination of these:

# os.O_RDONLY − open for reading only
# os.O_WRONLY − open for writing only
# os.O_RDWR − open for reading and writing
# os.O_NONBLOCK − do not block on open
# os.O_APPEND − append on each write
# os.O_CREAT − create file if it does not exist
# os.O_TRUNC − truncate size to 0
# os.O_EXCL − error if create and file exists
# os.O_SHLOCK − atomically obtain a shared lock
# os.O_EXLOCK − atomically obtain an exclusive lock
# os.O_DIRECT − eliminate or reduce cache effects
# os.O_FSYNC − synchronous writes
# os.O_NOFOLLOW − do not follow symlinks


# 38. os.openpty() in Python is a function used to create a pseudo-terminal, which consists of a pair of 
# file descriptors: one for the master end and one for the slave end of the terminal.
# A pseudo-terminal is a virtual terminal that acts like a physical terminal (e.g., the command line 
# interface), allowing programs to communicate as if they were interacting with a real terminal. This is useful for
# simulating terminal behavior, controlling command-line programs programmatically, and testing terminal-based applications.
# >>> m,s = os.openpty()
# >>> print(m)
# >>> print(s)
# >>> s = os.ttyname(s)
# >>> print(m)
# >>> print(s)
# or 
# master_fd, slave_fd = os.openpty()
# Data written to one end (master or slave) is received by the other end.

# Use Cases:
# Programmatically Controlling a Shell or Command:
# Simulate interaction with a shell (e.g., sending commands and reading responses).
# Testing Terminal Applications:
# Automate tests for programs that rely on terminal I/O.
# Custom Terminal-Based Interfaces:
# Build tools that intercept and manipulate terminal communication.
import os
# # Open a pseudo-terminal
# master_fd, slave_fd = os.openpty()
# # Write to the slave end (simulates user input in a terminal)
# os.write(slave_fd, b'Hello from slave end!\n')
# # Read from the master end (simulate terminal output to Python)
# output = os.read(master_fd, 1024)
# print(f"Master received: {output.decode()}")
# O/P - Master received: Hello from slave end!

# Real-World Example: Controlling a Shell
# This example shows how to run and control a shell (like /bin/bash) using os.openpty():
# import os
# import pty
# import subprocess

# # Open a pseudo-terminal
# master_fd, slave_fd = os.openpty()

# # Start a shell using the slave end of the pty
# proc = subprocess.Popen(['/bin/bash'], stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, close_fds=True)
# # Interact with the shell via the master_fd
# os.write(master_fd, b'echo Hello from the shell!\n')
# output = os.read(master_fd, 1024)
# print(f"Shell output: {output.decode()}")
# # Clean up
# proc.terminate()
# os.close(master_fd)
# os.close(slave_fd)



# os.pathconf() is a function in Python that retrieves system configuration values related to
#  a specific file or directory. It is used to query limits and settings that apply to filesystems, such as the maximum file
#  name length or maximum number of symbolic links that can be followed.
# Sample usage:
# >>> print(f"{os.pathconf_names}" )
# >>> no = os.pathconf('a2.py', 'PC_NAME_MAX')
# >>> print(f"Maximum length of a filename: {no}")
# >>> no = os.pathconf('a2.py', 'PC_FILESIZEBITS')
# >>> print(f"file size in bits: {no}")
# path: The file or directory path to query.
# name: The name of the configuration setting to retrieve. These are constants from the os module (e.g., os.pathconf_names).
# print(os.pathconf_names)
# Common Configuration Names:
# The os.pathconf_names dictionary contains the valid names you can use with os.pathconf. Some commonly used names are:
# Name	Description
# 'PC_NAME_MAX'	Maximum length of a filename in the directory.
# 'PC_PATH_MAX'	Maximum length of a relative path.
# 'PC_PIPE_BUF'	Maximum size of data written atomically to a pipe.
# 'PC_LINK_MAX'	Maximum number of hard links to a file.
# 'PC_NO_TRUNC'	Whether file names longer than NAME_MAX are truncated.
# Example Usage:
# 1. Checking Maximum File Name Length
# import os
# # Query the maximum file name length for the current directory
# max_name_length = os.pathconf('.', 'PC_NAME_MAX')
# print(f"Maximum file name length: {max_name_length}")
# 2. Checking Maximum Path Length
# import os
# # Query the maximum relative path length
# max_path_length = os.pathconf('.', 'PC_PATH_MAX')
# print(f"Maximum relative path length: {max_path_length}")
# 3. Using a File Path
# import os
# # Query configuration for a specific file
# file_path = '/tmp/example_file'
# name_max = os.pathconf(file_path, 'PC_NAME_MAX')
# print(f"Maximum file name length for {file_path}: {name_max}")
# Error Handling:
# If the specified name is invalid or unsupported on the system, os.pathconf() raises an OSError.
# Use Cases:
# Filesystem-Aware Programming:
# Writing programs that adapt to the filesystem's constraints (e.g., ensuring filenames or paths do not exceed the supported length).
# Portable Code:
# Ensuring compatibility across different platforms by querying limits dynamically instead of hardcoding them.
# Resource Management:
# Understanding limits on pipes, links, or other filesystem attributes when working with files or interprocess communication.





# 40.os.pipe() is a function in Python that creates a unidirectional communication channel between processes, 
# often referred to as a pipe. It provides two file descriptors—one for writing and one for reading—allowing 
# data written to one end of the pipe to be read from the other.
# r, w = os.pipe()
# r: File descriptor for the read end of the pipe.
# w: File descriptor for the write end of the pipe.
#  pipe can only transfer data in one direction:

# Data written to the write end (w) can be read from the read end (r).
# Communication is synchronized: the reader waits for data to be written, and the writer waits for space in the pipe buffer if it's full.

# Use Cases:
# Inter-Process Communication (IPC):
# Allow one process to send data to another process (e.g., parent and child processes).
# Connecting Program Components:
# Pass data from one program component to another in a producer-consumer setup.
# Simulating Simple Message Passing:
# Transfer information between different parts of a program or between scripts.
# Real-World Example: Parent chield communication
# import os
# # Create a pipe
# r, w = os.pipe()
# # Fork a new process
# pid = os.fork()
# if pid == 0:  # Child process
#     os.close(w)  # Close the write end in the child
#     message = os.read(r, 1024).decode()
#     print(f"Child received: {message}")
#     os.close(r)
# else:  # Parent process
#     os.close(r)  # Close the read end in the parent
#     os.write(w, b"Hello from parent!")
#     os.close(w)
# When to Use os.pipe:
# Use os.pipe() when you need lightweight, low-level communication between processes or different parts of your program.
# For more complex scenarios, consider using higher-level abstractions like multiprocessing.Pipe or subprocess for easier process management and communication.

# 41. popen os.popen(command, mode='r', buffering=-1)
# The os.popen() function in Python is used to open a pipe to or from a command that is executed in the operating system shell.
# This allows you to run external system commands and capture their output or send input to them.
# command: The shell command to execute as a string (e.g., "ls -l", "cat file.txt").
# mode:
# 'r' (default): Opens the pipe for reading the command’s output.
# 'w': Opens the pipe for writing to the command’s input.
# buffering: Controls the buffering of the pipe. Defaults to line-buffered (buffering=-1).
# Returns: A file-like object that can be used to read from or write to the command's input/output.

# Use Cases
# Executing System Commands: Run shell commands from within Python.
# Capturing Command Output: Read the output of commands like ls, df, or cat.
# Sending Input to Commands: Provide data to commands like grep or sort via the pipe.

# import os
# # Run the 'ls' command to list files in the current directory
# process = os.popen("ls")
# output = process.read()
# process.close()
# print("Command Output:")
# print(output)
# or
# # Run 'ls | grep file' to find files with "file" in their name
# process = os.popen("ls | grep file")
# output = process.read()
# process.close()
# print(output)

# Comparison with subprocess
# While os.popen() is simple to use, it is considered less secure and less versatile compared to the subprocess module. For most use cases, it’s recommended to use subprocess.
# Why Use subprocess Instead?
# Better Control: subprocess provides fine-grained control over input/output streams and command execution.
# Security: os.popen() uses the system shell by default, which can be unsafe if user input is passed to the command (risk of shell injection).
# Deprecation Warning: While not officially deprecated, os.popen() is discouraged in favor of subprocess.


# 43. readlink(path)
# # will return a string denoting the path to which the symbolic link points. It may return a relative or an absolute pathname.
# >>> src = '/usr/bin/python'
# >>> dst = '/tmp/python'
# >>> os.symlink(src, dst)
# >>> path = os.readlink( dst )
# >>> print(path)


# 44. remove(path)
# removes the specified file path. If that path is a directory, it raises an OSError
# >>> print(f"The dir is: {os.listdir(os.getcwd())}")
# >>> os.remove("aa.txt")
# >>> print(f"The dir after removal of path: {os.listdir(os.getcwd())}")

# 45. removedirs(path)
# This Python os Module will remove directories recursively.
# And if we successfully remove the leaf directory, it attempts to successively remove every parent directory displayed in that path.
# >>> print(f"The dir is: {os.listdir(os.getcwd())}")
# >>> os.removedirs("/tutorialsdir")
# >>> print(f"The dir after removal is: {os.listdir(os.getcwd())}")

# 46. rename(src,dst)
# rename() renames a file or directory. If the destination is a file or a directory that already exists, it raises an OSError.
# >>> print(f"The dir is: {os.listdir(os.getcwd())}”)
# >>> os.rename("tutorialsdir","tutorialsdirectory")
# >>> print(“Successfully renamed”)
# >>> print(f"The dir is: {os.listdir(os.getcwd())}")

# 47. renames(old,new)
# renames() Python os Module renames directories and files recursively.

# It is like os.rename(), but it also moves a file to a directory, or a whole tree of directories, that do not already exist.
# >>> print("Current directory is: { os.getcwd()}")
# >>> print("The dir is: { os.listdir(os.getcwd())}")
# >>> os.renames("aa1.txt","newdir/aanew.txt")
# >>> print("Successfully renamed”)
# >>> print(f"The dir is: {os.listdir(os.getcwd())}")

# # 48. rmdir(path)
# >>> print(f"the dir is: { os.listdir(os.getcwd())}")
# >>> os.rmdir("mydir")
# >>> print(f"the dir is: { os.listdir(os.getcwd())}"

# 49. stat(path)
# Use Cases
# File Size Check:
# Determine if a file exceeds a certain size.
# Timestamps:
# Check when a file was last modified (st_mtime) or accessed (st_atime).
# Permissions:
# Validate or modify file permissions (st_mode).
# Ownership:
# Check which user or group owns a file (st_uid, st_gid).
# File System Details:
# Inspect inode numbers (st_ino) or device IDs (st_dev)

# st_mode − protection bits
# st_ino − inode number
# st_dev − device
# st_nlink − number of hard links
# st_uid − user id of owner
# st_gid − group id of owner
# st_size − size of file, in bytes
# st_atime − time of most recent access
# st_mtime − time of most recent content modification
# st_ctime − time of most recent metadata change.
# Sample usage:

# >>> statinfo = os.stat('a2.py')
# >>> print(statinfo)

# Difference Between os.stat and os.lstat
# os.stat(path):
# Follows symbolic links (gets metadata of the target).
# os.lstat(path):
# Does not follow symbolic links (gets metadata of the symlink itself).

# Example Usage
# 1. Retrieve File Metadata 
# import os
# # Get metadata about a file
# file_stats = os.stat("example.txt")
# # Print file size and last modification time
# print("File Size:", file_stats.st_size, "bytes") # File Size: 2048 bytes
# Time values are always returned as floating-point numbers after 3.8
# print("Last Modified:", file_stats.st_mtime) # Last Modified: 1674059386.123456 

# # Check if the file is readable by the owner
# is_readable = bool(file_stats.st_mode & stat.S_IRUSR)
# print("Is the file readable by the owner?", is_readable)
# # To get metadata about the symlink itself, use follow_symlinks=False:
# symlink_metadata = os.stat("example_symlink", follow_symlinks=False)
# print("Symlink Metadata:", symlink_metadata)

# 50. statvfs(path)
# retrieves information about the file system containing a given path. It provides details such as
# the size of the file system, available space, and block size, making it useful for analyzing disk usage and capacity.
# ** This function is specific to Unix-like systems (e.g., Linux, macOS). It may not be available on Windows.
# Attribute	Description
# f_bsize	File system block size (used for transfers).
# f_frsize	Fragment size (smallest unit of allocation).
# f_blocks	Total number of blocks in the file system.
# f_bfree	Number of free blocks in the file system.
# f_bavail	Number of free blocks available to non-superuser processes.
# f_files	Total number of file inodes in the file system.
# f_ffree	Number of free inodes in the file system.
# f_favail	Number of free inodes available to non-superuser processes.
# f_flag	File system flags (e.g., read-only status).
# f_namemax	Maximum filename length allowed on the file system.

# Get file system stats for the root directory
# fs_stats = os.statvfs("/")
# # Calculate disk space in bytes
# block_size = fs_stats.f_frsize
# total_space = fs_stats.f_blocks * block_size
# free_space = fs_stats.f_bfree * block_size
# available_space = fs_stats.f_bavail * block_size
# print(f"Total Space: {total_space / (1024**3):.2f} GB")
# print(f"Free Space: {free_space / (1024**3):.2f} GB")
# print(f"Available Space: {available_space / (1024**3):.2f} GB")
# # Get file system stats for the root directory
# fs_stats = os.statvfs("/")
# # Check available inodes
# free_inodes = fs_stats.f_ffree
# print(f"Free Inodes: {free_inodes}")

# 51. symlink(src,dst)
# symlink() composes a symbolic link dst that points to the source.
# Cross-File-System Linking:
# Symlinks can point to targets on different file systems.
# If the src file or directory is deleted or moved, the symlink becomes a "broken link."
# os.symlink(src, dst, target_is_directory=False)
# if os.path.islink("example_symlink"):
#     print("This is a symlink!")
# else:
#     print("This is not a symlink.")
# if os.path.islink(symlink) and not os.path.exists(symlink):
#     print("This symlink is broken!")
# Here’s the full list of relevant os methods for working with symlinks:
# os.path.islink(path)
# os.readlink(path)
# os.symlink(src, dst)
# os.remove(path)
# os.lstat(path)
# os.path.abspath(path)
# os.path.exists(path)
# os.path.lexists(path)
# os.rename(src, dst)
# os.listdir(path)
# os.lchown(path, uid, gid)
# os.lchmod(path, mode) (platform-specific)
# os.stat(path) (follows the symlink by default)

# 52. os.tcgetpgrp(fd) Limitation- 1.works only on terminal 2. Unix-specific
# retrieves the process group ID (PGID) of the foreground process group for a given terminal file descriptor (fd). This is useful when working with terminal control in Unix-like operating systems.
# What is a Process Group in Terminals?
# A process group is a collection of processes identified by a process group ID (PGID).
# Each terminal has a foreground process group, which is the group of processes currently interacting with the terminal (e.g., a shell or program running in the terminal).
# Background processes running in the same terminal are not part of the foreground process group.
# How os.tcgetpgrp Works
# It queries the terminal associated with the file descriptor (fd) and returns the PGID of the foreground process group.
# This is often used in terminal or job control scenarios, such as determining which process group currently has control of a terminal.
# OSError: If the file descriptor is invalid or does not refer to a terminal device.
# fd: A file descriptor referring to a terminal device (e.g., a terminal session). You can get this file descriptor using functions like os.open() or sys.stdin.fileno().
# Example Usage
# 1. Get Foreground Process Group ID
# # Get the file descriptor for the current terminal
# fd = os.open("/dev/tty", os.O_RDWR)
# # Get the foreground process group ID
# pgid = os.tcgetpgrp(fd)
# print("Foreground Process Group ID:", pgid)
# os.close(fd)
# or
# # Get the foreground process group ID of the terminal connected to stdin
# pgid = os.tcgetpgrp(sys.stdin.fileno())
# print("Foreground Process Group ID:", pgid)

# Related Methods
# os.tcsetpgrp(fd, pgid):
# Sets the foreground process group of the terminal referred to by fd to the specified pgid.
# os.getpgrp():
# Returns the PGID of the calling process.
# os.setpgid(pid, pgid):
# Sets the process group ID for a specific process (pid).

# 53. tcsetpgrp(fd, pg)
# function in Python is used to set the foreground process group of a terminal. It assigns control of the terminal referred to by the file descriptor
# which is an open file descriptor, and is returned by os.open(), to pg.
# (fd) to the specified process group ID (pg). This is commonly used in job control for managing foreground and background processes in terminal applications or shells.
# fd: A file descriptor that refers to a terminal device (e.g., /dev/tty or sys.stdin.fileno()).
# pg: The process group ID (PGID) to be set as the foreground process group for the terminal.


# 55. ttyname(fd)
# ttyname() Python os Module  will return a string that denotes the terminal device linked to the descriptor fd.
# If it isn’t linked to a terminal device, it raises an exception
# >>> print(f"Current working dir : { os.getcwd()}")
# >>> fd = os.open("/dev/tty",os.O_RDONLY)
# >>> p = os.ttyname(fd)
# >>> print(f"the terminal device associated is: {p}")
# >>> os.close(fd)

# 56. unlink(path)
# This Python os Module will remove specified file path. If it is a directory, it raises an OSError.
# >>> print(f"The dir is: { os.listdir(os.getcwd())}")
# >>> os.unlink("aa.txt")
# >>> print(f"The dir after removal of path : { os.listdir(os.getcwd())}")

# 57. utime(path,times)
# Python os Module utime() sets the access and modified times of the file at the specified path.
# >>> stinfo = os.stat('a2.py')
# >>> print(stinfo)
# >>> print(f"access time of a2.py: { stinfo.st_atime }")
# >>> print(f"modified time of a2.py: { stinfo.st_mtime }")
# >>> os.utime("a2.py",(1330712280, 1330712292))


# 58.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# walk() creates file names in a directory tree. It does so by walking the tree either bottom-up or top-down.

# It has the following parameters:

# top − Each directory rooted at directory
# topdown − If topdown is True, or not specified, it scans directories top-down.
# onerror − This may show an error to continue with the walk, or may raise an exception to abort the walk.
# followlinks − This will visit directories that symlinks points to, that is, if set to true.
# Sample usage:

# >>> for root, dirs, files in os.walk(".", topdown=False):
# OUTPUT
# for name in files:
# print(os.path.join(root, name))
# for name in dirs:
# print(os.path.join(root, name))

# 59.write(fd,str)   
# write(fd,str)
# This Python os Module  will write the specified string to descriptor fd. It returns the number of bytes that it actually wrote.
# >>> fd = os.open("f1.txt",os.O_RDWR|os.CREAT)
# >>> ret = os.write(fd,"This is test")
# >>> print(f"the number of bytes written: {ret}")
# >>> print("written successfully")
# >>> os.close(fd)