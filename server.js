const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = process.env.PORT || 4000;
const python = process.env.PYTHON || 'python';

const bot = spawn(python, ['main.py'], {
  cwd: __dirname,
  stdio: ['ignore', 'pipe', 'pipe'],
});

bot.stdout.on('data', data => {
  console.log(`Bot: ${data}`);
});

bot.stderr.on('data', data => {
  console.error(`Bot error: ${data}`);
});

bot.on('error', error => {
  console.error(`Failed to start bot using "${python}":`, error);
});

bot.on('exit', code => {
  console.log(`Bot exited with code ${code}`);
});

app.get('/', (req, res) => {
  res.send('Telegram AI Bot is running!');
});

const server = app.listen(port, '0.0.0.0', () => {
  console.log(`Server listening on port ${port}`);
});

for (const signal of ['SIGINT', 'SIGTERM']) {
  process.on(signal, () => {
    server.close();
    if (bot.exitCode === null && !bot.killed) {
      bot.kill(signal);
    }
  });
}
