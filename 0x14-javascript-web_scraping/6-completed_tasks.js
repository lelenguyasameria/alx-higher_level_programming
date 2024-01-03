#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const todosData = JSON.parse(body);

      // Create a map to store the number of completed tasks for each user
      const completedTasksByUser = new Map();

      // Filter only completed tasks and count them for each user
      todosData.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId;
          completedTasksByUser.set(userId, (completedTasksByUser.get(userId) || 0) + 1);
        }
      });

      // Print users with completed tasks
      completedTasksByUser.forEach((completedTasks, userId) => {
        console.log(`User ${userId} has completed ${completedTasks} tasks.`);
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

