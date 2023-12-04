#![allow(dead_code)]
#![allow(unused_variables)]

use std::cmp::max;
use crate::helper::Data;


pub fn start(){
    let data:Data = Data::new(4,1);
    let mut sum = 0;
    let mut count = 1;
    data.input.lines().for_each(|line|{
        let all:Vec<&str> = line.split(" ").map(|s|s.trim()).collect();
        let split_index = all.iter().position(|s| *s == "|").unwrap();
        let winning: Vec<u32> = all[2..split_index]
            .iter()
            .filter_map(|s| s.parse::<u32>().ok())
            .collect();
        let card:Vec<u32> = all[split_index..]
            .iter()
            .filter_map(|num| num.parse::<u32>().ok())
            .collect();
        let mut matches:i32 = 0;
        winning.iter().for_each(|&w|{
           let is: Vec<_> = card
               .iter()
               .filter(|&&c|c == w)
               .cloned()
               .collect();
            if is.len() > 0 {
                matches += 1;
            }
        });
        let t:u32 = 2;
        let mut points:f32 = 2i32.pow(matches as f32 as u32) as f32 / 2.0;
        points = points.floor();

        println!("Card: {} Matches:{} Points:{}", count, matches, points);
        sum += points as i32;
        count += 1;
    });
    println!("SUM:{}",sum);

}