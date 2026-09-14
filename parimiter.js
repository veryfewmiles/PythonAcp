let shape = prompt("What shape do you want? rectangle or square")
shape = shape.toLowerCase()
if (shape == "rectangle") {
    let length = Number(prompt("Enter the length: "))
    let width = Number(prompt("Enter the width: "))
    let perimeter = (length + width) * 2
    console.log("Rectangle perimeter:", perimeter)
    alert("The perimeter is " + perimeter)
} else if (shape == "square") {
    let side = Number(prompt("Enter the side length: "))
    let perimeter = side * 4
    console.log("Square perimeter:", perimeter)
    alert("The perimeter is " + perimeter)
} else {
    
    console.log("Invalid shape")
    alert("Please enter rectangle or square")
}