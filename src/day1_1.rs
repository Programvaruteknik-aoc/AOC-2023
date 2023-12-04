#![allow(dead_code)]
#![allow(unused_variables)]
use std::fs;

pub fn is_digit(c: char) -> bool {
    c >= '0' && c <= '9'
}

pub fn start(){

    let contents = fs::read_to_string("./src/inputs/day1/day1_input1.txt")
        .expect("Could not read file");
    let mut sum:i64 = 0;
    let mut a:char = char::from(0);
    let mut b:char = char::from(0);
    for line in contents.lines(){
        line.chars().enumerate().for_each(|c|{
            if c.1 >= '0' && c.1 <= '9' {
                if a == char::from(0){
                    a = c.1;
                }
                b = c.1;
            }

        });
            //

            let str:String = a.to_string() + &*b.to_string();
            match str.parse::<i64>() {
                Ok(parsed) => {
                    sum += parsed;
                }
                Err(err) => {
                    println!("Bajs");
                }
            }
            println!("Found a:{a} b:{b}");
            a = char::from(0);
            b = char::from(0);



    }

    println!("Contents:\n{contents}");
    println!("SUM: {sum}");

}