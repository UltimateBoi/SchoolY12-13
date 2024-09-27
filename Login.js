const fs = require('fs'), rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });
const loadUserDetails = filePath => JSON.parse(fs.readFileSync(filePath, 'utf8'));
const checkUserId = (userId, storedUserId) => userId === storedUserId;
const checkPin = (pin, storedPin) => pin === storedPin;

const login = userDetails => {
  let attempts = 0, maxAttempts = 3;
  const ask = (question, cb) => rl.question(question, answer => cb(answer));
  const checkPassword = () => {
    if (attempts >= maxAttempts) return console.log("Incorrect password - access denied"), rl.close();
    const positions = Array.from({ length: 3 }, () => Math.floor(Math.random() * userDetails.password.length) + 1);
    ask(`Enter characters ${positions.join(', ')} of your password: `, answer => {
      if (positions.every((pos, i) => answer[i] === userDetails.password[pos - 1])) return console.log("Access granted"), rl.close();
      else attempts++, console.log(`Incorrect password - access denied. You have ${maxAttempts - attempts} attempts left.`), checkPassword();
    });
  };
  const checkPin = () => {
    if (attempts >= maxAttempts) return console.log("Incorrect PIN - access denied"), rl.close();
    ask("Enter your 4-digit PIN: ", pin => {
      if (checkPin(pin, userDetails.pin)) checkPassword();
      else attempts++, console.log(`Incorrect PIN - access denied. You have ${maxAttempts - attempts} attempts left.`), checkPin();
    });
  };
  const checkUserId = () => {
    if (attempts >= maxAttempts) return console.log("Incorrect ID - access denied"), rl.close();
    ask("Enter your 10-character user ID: ", userId => {
      if (checkUserId(userId, userDetails.user_id)) checkPin();
      else attempts++, console.log(`Incorrect ID - access denied. You have ${maxAttempts - attempts} attempts left.`), checkUserId();
    });
  };
  checkUserId();
};

login(loadUserDetails('user_details.json'));