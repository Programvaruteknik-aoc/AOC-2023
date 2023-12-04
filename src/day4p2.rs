#![allow(dead_code)]
#![allow(unused_variables)]

use std::cmp::max;
use std::fs::copy;
use std::str::Lines;
use crate::helper::Data;
fn get_consecutives_for_card(data:&str) -> Vec<i32> {
    let card = data;
    let card_id:i32 = data.split_once(":")
        .unwrap().0
        .split_once(" ")
        .unwrap().1
        .trim()
        .parse()
        .unwrap();
    let matches= get_number_matches_for_card(data);
    let mut consecutives:Vec<i32> = Vec::new();
    for i in 0..matches{
        consecutives.push(card_id + i + 1);
    }
    // print!("Card ID:{} matches: ",card_id);
    // consecutives.iter().for_each(|con|{
    //     print!("{} ",con);
    // });
    // println!();
    consecutives
}
fn get_number_matches_for_card(data:&str) -> i32 {
    let card = data;
    let all: Vec<&str> = card.split(" ").map(|s| s.trim()).collect();
    let split_index = all.iter().position(|s| *s == "|").unwrap();

    let winning: Vec<i32> = all[2..split_index]
        .iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    let card: Vec<i32> = all[split_index..]
        .iter()
        .filter_map(|num| num.parse::<i32>().ok())
        .collect();

    let mut matches:i32 = 0;
    winning.iter().for_each(|&w| {
        let is: Vec<_> = card
            .iter()
            .filter(|&&c| c == w)
            .cloned()
            .collect();
        if is.len() > 0 {
            matches += 1;
        }
    });
    matches
}

pub fn start(){
    let data:Data = Data::new(4,1);
    let mut lines:Vec<&str> = data.input.lines().collect();
    let mut sum = 0;
    let mut count:i32 = 1;
    let mut scratchcards:i32 = 0;
    let mut total:Vec<i32> = Vec::new();
    let mut que:Vec<i32> = Vec::new();
    lines.iter().for_each(|line|{que.push(count); count += 1;});

    // lines.iter().for_each(|line| {
    //    println!("{}",line);
    // });
    while !que.is_empty() {
        let matches = get_consecutives_for_card(lines.get(0).unwrap());
        let mut que_clone = que.clone();
        let mut submatch: Vec<i32> = Vec::new();
        que_clone.iter().for_each(|item| {
            let i = (item - 1) as usize;
            //println!("Que[{}]", i);
            //println!("[{} ]", lines.get(i).unwrap());
            submatch.extend(get_consecutives_for_card(lines.get(i).unwrap()));
        });
        total.extend(que_clone.clone());
        que_clone.clear();
        que.clear();
        que.extend(submatch);
    }
    total.iter().for_each(|item|{
        print!("{} ",item);
    });
    //scratchcards += data.example.lines().count() as i32;
    println!("scratchcards:{}", scratchcards);
    println!("SUM:{}",total.len());
}