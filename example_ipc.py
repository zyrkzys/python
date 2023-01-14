import os
import time

# Create a pipe
pipe_fd = os.pipe()

# Fork the process
pid = os.fork()

if pid == 0:
    pid = os.getpid()
    # This is the child process
    # Close the write end of the pipe
    os.close(pipe_fd[1])
    # Read from the pipe
    message = os.read(pipe_fd[0], 1024)
    print(int(time.time()),": PID:", pid, ": Child process received:", message.decode())
else:
    pid = os.getpid()
    # This is the parent process
    # Close the read end of the pipe
    os.close(pipe_fd[0])
    # Write to the pipe
    message = "Hello from the parent!"
    os.write(pipe_fd[1], message.encode())
    # Wait for the child to finish
    print(int(time.time()),": PID:", pid, ": Parent process sent:", message)
    # os.wait(1)
