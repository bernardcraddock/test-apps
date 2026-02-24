// DOMContentLoaded ensures script runs after HTML loaded
//  event, function, capture
document.addEventListener("DOMContentLoaded", function() {
    
    // Select title element by id
    const titleElement = document.getElementById("title");

    // Select input element
    const inputElement = document.getElementById("input");

    // Select the save button
    const saveButton = document.getElementById("saveButton");

    // Select the delete button
    const deleteButton = document.getElementById("deleteButton");


    // 1st Load any previously save value from Browser local storage so is displayed straight away
    console.log("retrieving from local storage");
    const savedValue = localStorage.getItem("inputValue");
    if (savedValue) {
        inputElement.value = savedValue;
        titleElement.innerHTML = savedValue;
    }

    // Add event listener to the input element
    inputElement.addEventListener("input", function() {

        // Update titleElement inner HTML with the input value
        // or f input value is empty
        // empty set meaningful user friendly fallback value
        // innerHTML property element represent the html contents inside that element tags text etc  
        titleElement.innerHTML = inputElement.value || "Original Title"; 
    });

    // Add event listener to the saveButton that saves inputValue to local storage 
    saveButton.addEventListener("click", function() {
        // save input value to local storage
        localStorage.setItem("inputValue", inputElement.value);
        console.log("saving:", inputElement.value, "to local storage");
        alert("input value saved");
    });

    deleteButton.addEventListener("click", function() {
        localStorage.removeItem("inputValue");
        console.log("removing:", inputElement.value, "from local storage");
 
        // removes all localStorage data not just specific key
        localStorage.clear(); 

        // clear input field and reset orginal title
        inputElement.value = "";
        titleElement.innerHTML = "Original Title";
        console.log("restoring original title");
    });

});