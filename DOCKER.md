# Getting Started with Docker

This guide provides instructions on how to start the Browseek library using Docker.

## Prerequisites

- Docker: Make sure you have Docker installed on your system. You can download and install Docker from the official website: https://www.docker.com/get-started

## Steps

1. Clone the Browseek repository:
   ```
   git clone https://github.com/yourusername/browseek.git
   ```

2. Navigate to the project directory:
   ```
   cd browseek
   ```

3. Build the Docker image:
   ```
   docker-compose build
   ```

4. Run the Docker container:
   ```
   docker-compose up
   ```

   This command will start the Browseek library and the example Nginx server.

5. Access the example webpage:
   Open your web browser and visit https://example.local

   You should see the example webpage served by the Nginx server, which includes some text and images.

6. Run the Browseek library:
   You can now use the Browseek library within the Docker container. The library is accessible at the `browseek` service.

   For example, you can run the `examples/docker_example.py` script:
   ```
   docker-compose exec browseek python examples/docker_example.py
   ```

   This script demonstrates how to use the Browseek library to perform a simple task on the example webpage.

7. Stop the Docker container:
   To stop the running container, press `Ctrl+C` in the terminal where you ran `docker-compose up`.

   Alternatively, you can run the following command in a separate terminal:
   ```
   docker-compose down
   ```

That's it! You have successfully started the Browseek library using Docker and accessed the example webpage served by the Nginx server.

For more information on using the Browseek library and its features, please refer to the documentation and examples provided in the repository.
