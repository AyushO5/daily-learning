function One () {
    console.log("Inside function one") 
    Two()
}

function Two () {
    console.log("Inside function two")
    Three()
}

function Three () {
    console.log("Inside function three")

}

One()