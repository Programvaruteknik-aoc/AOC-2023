use num::Integer;
use crate::day5p2::parse_numbers;
use crate::helper::Data;

pub fn calc(time:i64, dist:i64) -> usize {
    let mut result:Vec<i64> = Vec::new();
    for pressed in 0..=time {
        let distance = pressed*(time -pressed);
        if distance > dist {
            result.push(distance);
        }
    }
    result.len()
}

pub fn start(){
    let data:Data = Data::new(6,1);
    let mut lines:Vec<&str> = Vec::new();
    data.input.lines().for_each(|line|{
        lines.push(line);
    });

    let times = parse_numbers(lines.get(0).unwrap().split_once(":").unwrap().1);
    let dists = parse_numbers(lines.get(1).unwrap().split_once(":").unwrap().1);

    let mut races:Vec<usize> = Vec::new();
    times.iter().enumerate().for_each(|race| {
        races.push(calc(*race.1 as i64, *dists.get(race.0).unwrap() as i64));
    });
    let mut product:u64 = 1;
    for race in races{
        product *= race as u64;
        println!("{}",race);
    }
    println!("Product: {}",product);
}