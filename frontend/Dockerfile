# Use the official Nginx image to serve static files
FROM nginx:stable-alpine

# Remove the default Nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy your static frontend files to Nginx's html directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
