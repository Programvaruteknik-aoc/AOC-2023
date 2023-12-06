use std::fmt::format;
use crate::day5p2::parse_numbers;
use crate::day6p1;
use crate::helper::Data;

pub fn start(){
    let data:Data = Data::new(6,2);
    let mut lines:Vec<&str> = Vec::new();
    data.input.lines().for_each(|line|{
        lines.push(line);
    });

    let times = parse_numbers(lines.get(0).unwrap().split_once(":").unwrap().1);
    let dists = parse_numbers(lines.get(1).unwrap().split_once(":").unwrap().1);

    let mut t:String = String::new();
    let mut d:String = String::new();
    for time in times{
        t = format!("{}{}", t, time.to_string());
    }
    for dist in dists{
        d = format!("{}{}", d, dist.to_string());
    }
    let mut races:Vec<usize> = Vec::new();
    let res = day6p1::calc(t.parse::<i64>().unwrap(),d.parse::<i64>().unwrap());
    let mut product:u64 = 1;
    for race in races{
        product *= race as u64;
        println!("{}",race);
    }
    println!("Product: {}",res);
}