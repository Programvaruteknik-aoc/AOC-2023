use std::arch::aarch64::vld1_dup_f32;
use std::collections::HashMap;
use crate::helper::Data;
enum Types {
    RED = 12,
    GREEN = 13,
    BLUE = 14
}
pub fn start(){
    let data = Data::new(2,1);

    let red = 12;
    let green = 13;
    let blue = 14;
    let mut sum = 0;
    for line in data.input.lines(){
        let first:Vec<&str> = line.split(":").collect();
        let mut game_id:i32 = 0;
        let mut sets:Vec<&str> = vec![];
        if let Some(substring) = first.get(0) {
            let game_str:Vec<&str> = substring.split_whitespace().collect();
            if let Some(game_id_str) = game_str.get(1){
                game_id = game_id_str.parse::<i32>().unwrap();
            }
        }
        if let Some(game_str) = first.get(1) {
            println!("Games {}",game_str);
            let games:Vec<&str> = game_str.split(";").collect();
            let mut passed = true;
            games.iter().for_each(|round| {
                println!("\tRound [{}]",round);
                let round:Vec<&str> = round.split(",").map(|v| v.trim()).collect();
                round.iter().for_each(|set| {
                    println!("\t\tSet [{}]",set);
                    let play_str:Vec<&str> = set.split(" ").collect();
                    if play_str.len() == 2 {
                        let key = play_str.get(0).unwrap().parse::<i32>().unwrap();
                        let value = play_str.get(1).unwrap();
                        let limit:i32 = match value {
                            &"red" => Types::RED as i32,
                            &"green" => Types::GREEN as i32,
                            &"blue" => Types::BLUE as i32,
                            _ => -1
                        };
                        if key > limit{
                            passed = false;
                        }
                        println!("\t\t\tK [{}] V [{}]",key,value);
                    }
                });
            });
            if passed {
                sum += game_id;
            }
        }
    }

    println!("SUM:{} ",sum);

}