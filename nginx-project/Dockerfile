# Use the official nginx base image
FROM nginx:1.19-alpine

# Copy custom configuration file from the host to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]