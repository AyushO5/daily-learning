// console.log(this)

const user = {
  name: "Ayush",
  greet() {
    console.log(this.name);
  }
};

user.greet(); // Ayush


function show () {
console.log(this) ;
}

show()


const user2 = {
  name: "Ayush",
  greet: () => {
    console.log(this.name);
  }
};

user2.greet(); // undefined


const user3 = {
  name: "Ayush",
  greet: () => {
    console.log(this.name);
  }
};

user3.greet(); // undefined


const user4 = {
  name: "Ayush",
  greet() {
    const inner = () => {
      console.log(this.name);
    };
    inner();
  }
};

user4.greet(); // Ayush
