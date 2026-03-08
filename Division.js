// Function to perform division of two numbers
function divide(a, b) {
    if (b === 0) {
        return "Division by zero is not allowed";
    }
    return a / b;
}

// Example usage: Divide numbers from 1 to 999 by 2
for (let i = 1; i <= 999; i++) {
   console.log(`Division of ${i} by 2: ${divide(i, 2)}`);
}