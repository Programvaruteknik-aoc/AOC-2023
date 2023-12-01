use std::collections::HashMap;
use std::ptr::null;
use std::str::Chars;
use crate::day1_1::is_digit;
use crate::helper::Data;

fn check_for_word(line:String) -> Vec<char>{
    let mut matches:Vec<char> = Vec::new();
    let mut words = HashMap::new();
    words.insert("zero" , '0');
    words.insert("one"  , '1');
    words.insert("two"  , '2');
    words.insert("three", '3');
    words.insert("four" , '4');
    words.insert("five" , '5');
    words.insert("six"  , '6');
    words.insert("seven", '7');
    words.insert("eight", '8');
    words.insert("nine" , '9');
    words.iter().for_each(|word|{
       if( line.starts_with(word.0)){
           println!("Word match");
           matches.push(*word.1);
       }
    });
    matches
}

pub fn start(){

    let data = Data::new(1,2);
    let mut sum:i64 = 0;
    let mut a:char = char::from(0);
    let mut b:char = char::from(0);
    for line in data.input.lines(){
        line.chars().enumerate().for_each(|c|{
            let mut ch:char = char::from(0);
            let subline = line[c.0..].to_string();
            let word_check = check_for_word(subline);
            if is_digit(c.1) {
                ch = c.1;
            }
            else if !word_check.is_empty() {
                match word_check.get(0) {
                    Some(&element) => {
                        ch = element;
                    }
                    None => {
                        println!("Did not find any word match")
                    }
                }
            }
            if ch != char::from(0){
                if a == char::from(0){
                    a = ch;
                }
                b = ch;
            }
        });
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
    println!("{}",sum);
}