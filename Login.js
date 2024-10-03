const fs = require('fs'); // Import the file system module
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout }); // Create an interface for reading input and output

const loadUserDetails = filePath => JSON.parse(fs.readFileSync(filePath, 'utf8')); // Load user details from a JSON file
const checkUserId = (userId, storedUserId) => userId === storedUserId; // Check if the user ID matches the stored user ID
const checkPin = (pin, storedPin) => pin === storedPin; // Check if the PIN matches the stored PIN

const login = userDetails => { // Main login function
  let attempts = 0, maxAttempts = 3; // Initialize attempt counters

  const ask = (question, cb) => rl.question(question, cb); // Function to ask a question and get a response
  const denyAccess = message => { // Function to deny access and close the readline interface
    console.log(message); // Log the denial message
    rl.close(); // Close the readline interface
  };

  const checkPassword = () => { // Function to check the password
    if (attempts >= maxAttempts) return denyAccess("Incorrect password - access denied"); // Deny access if max attempts reached
    const positions = Array.from({ length: 3 }, () => Math.floor(Math.random() * userDetails.password.length) + 1); // Randomly select 3 positions in the password
    ask(`Enter characters ${positions.join(', ')} of your password: `, answer => { // Ask for specific characters of the password
      if (positions.every((pos, i) => answer[i] === userDetails.password[pos - 1])) return denyAccess("Access granted"); // Grant access if the characters match
      attempts++; // Increment attempts counter
      console.log(`Incorrect password - access denied. You have ${maxAttempts - attempts} attempts left.`); // Log incorrect password message
      checkPassword(); // Retry password check
    });
  };

  const checkPin = () => { // Function to check the PIN
    if (attempts >= maxAttempts) return denyAccess("Incorrect PIN - access denied"); // Deny access if max attempts reached
    ask("Enter your 4-digit PIN: ", pin => { // Ask for the PIN
      if (checkPin(pin, userDetails.pin)) return checkPassword(); // Proceed to password check if PIN matches
      attempts++; // Increment attempts counter
      console.log(`Incorrect PIN - access denied. You have ${maxAttempts - attempts} attempts left.`); // Log incorrect PIN message
      checkPin(); // Retry PIN check
    });
  };

  const checkUserId = () => { // Function to check the user ID
    if (attempts >= maxAttempts) return denyAccess("Incorrect ID - access denied"); // Deny access if max attempts reached
    ask("Enter your 10-character user ID: ", userId => { // Ask for the user ID
      if (checkUserId(userId, userDetails.user_id)) return checkPin(); // Proceed to PIN check if user ID matches
      attempts++; // Increment attempts counter
      console.log(`Incorrect ID - access denied. You have ${maxAttempts - attempts} attempts left.`); // Log incorrect ID message
      checkUserId(); // Retry user ID check
    });
  };

  checkUserId(); // Start the login process by checking the user ID
};

login(loadUserDetails('user_details.json')); // Load user details and start the login process