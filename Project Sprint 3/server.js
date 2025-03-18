const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const multer = require('multer');

// Set up multer storage
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/'); // Specify the directory to save uploaded files
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + '-' + file.originalname); // Append timestamp to the original file name
    }
});

const upload = multer({ storage: storage });
const app = express();
app.use(express.static(__dirname)); // Serve static files from the current directory

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Update the endpoint to handle file uploads
app.post('/report', upload.single('image'), (req, res) => {
    const newItem = {
        name: req.body['item-name'],
        description: req.body['description'],
        location: req.body['location'],
        date: req.body['date-lost'],
        time: req.body['time-lost'],
        image: req.file.path // Store the path of the uploaded image
    };

    // Read existing items
    fs.readFile('items.json', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading items file');
        }
        const items = JSON.parse(data);
        items.push(newItem);

        // Write updated items back to file
        fs.writeFile('items.json', JSON.stringify(items, null, 2), (err) => {
            if (err) {
                return res.status(500).send('Error saving item');
            }
            res.status(201).send('Item reported successfully');
        });
    });
});

// Endpoint to serve items
app.get('/items', (req, res) => {
    fs.readFile('items.json', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading items file');
        }
        res.json(JSON.parse(data));
    });
});

const PORT = 3000;

// Sample data storage
let users = [];

// Load users from file
const loadUsers = () => {
    const usersFilePath = path.join(__dirname, 'users.json');
    if (fs.existsSync(usersFilePath)) {
        const data = fs.readFileSync(usersFilePath);
        users = JSON.parse(data);
    }
};

// Save users to file
const saveUsers = () => {
    const usersFilePath = path.join(__dirname, 'users.json');
    fs.writeFileSync(usersFilePath, JSON.stringify(users, null, 2));
};

// Load users when the server starts
loadUsers();

let messages = [];

// User Registration
app.post('/register', (req, res) => {
    const { email, password, studentNumber, department, userLevel, firstName, middleInitial, lastName, suffix } = req.body;

    if (users.find(user => user.email === email)) {
        return res.status(400).json({ message: 'User already exists' });
    }
    console.log('Registering user:', { email, studentNumber }); // Log registration attempt
    users.push({ email, password, studentNumber, department, userLevel, firstName, middleInitial, lastName, suffix }); // Save additional user details

    try {
        saveUsers(); // Save users to file
    } catch (error) {
        console.error('Error saving user:', error);
        return res.status(500).json({ message: 'An error occurred while saving the user.' });
    }

    res.status(201).json({ message: 'User registered successfully' });
});

// User Login
app.post('/login', (req, res) => {
    const { email, password } = req.body;
    const user = users.find(user => user.email === email && user.password === password);
    if (!user) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }
    res.status(200).json({ message: 'Login successful' });
});

// Send Message
app.post('/messages', (req, res) => {
    const { recipient, message } = req.body;
    messages.push({ recipient, message });
    res.status(201).json({ message: 'Message sent' });
});

// Get Messages
app.get('/messages', (req, res) => {
    res.status(200).json(messages);
});

app.get('/', (req, res) => {
    res.send('Welcome to the Cardinal Lost & Found API!');
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
