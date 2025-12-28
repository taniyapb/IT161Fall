function assignedScore(score) { // assigned score function with 'score' parameter 
    if (score >= 90) { // if else statement to check argument
        return "Wow! You got an A";
    } else if (score >= 80) {
        return "Wow! You got a B";
    } else if (score >= 70) {
        return "Wow! You got a C";
    } else if (score >= 60) {
        return "Wow! You got a D";
    } else {
        return "Wow! You got an F";
    }
}

alert(assignedScore(95)); //calling the alert function
