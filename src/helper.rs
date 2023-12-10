use std::{fs};

pub struct Data{
    pub example:String,
    pub input:String
}



impl Data{
    pub fn new(day:i32, part:u8) -> Data{
        // fs::read_to_string("inputs/day1/day2_input1.txt")
        let d:String = day.to_string();
        let p:String = part.to_string();
        let dir:String = "./src/inputs/day".to_owned() + &*d + "/day" + &*d + "_";
        let in_path:String = dir.clone() + "input" + &*p + ".txt";
        let ex_path:String = dir.clone() + "example" + &*p + ".txt";
        // println!("{}",in_path);
        // println!("{}",ex_path);
        let example:String = fs::read_to_string(ex_path).expect("Could not read example file");
        let input:String = fs::read_to_string(in_path).expect("Could not read input file");
        Data{example, input}
    }
}