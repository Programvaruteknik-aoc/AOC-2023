use std::arch::aarch64::vld1_dup_f32;
use std::collections::HashMap;
use crate::helper::Data;
enum Types {
    RED = 12,
    GREEN = 13,
    BLUE = 14
}
pub fn start(){
    let data = Data::new(2,2);
    let mut tracker:HashMap<&str,i32> = HashMap::new();
    let mut sum = 0;
    let mut power:i32 = 0;
    for line in data.input.lines(){
        let first:Vec<&str> = line.split(":").collect();
        let mut game_id:i32 = 0;
        let mut sets:Vec<&str> = vec![];
        tracker.insert("red",0);
        tracker.insert("green",0);
        tracker.insert("blue",0);
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
                        if tracker.get(value).unwrap() < &key {
                            tracker.insert(value,key);
                        }
                        println!("\t\t\tK [{}] V [{}]",key,value);
                    }
                });
            });
            if passed {
                sum += game_id;
            }
            let p = tracker.get("red").unwrap() * tracker.get("green").unwrap() * tracker.get("blue").unwrap();
            println!("GAME {} -> P [{}]",game_id,p);
            power += p;
        }
        println!("POWER:{} ",power);
    }

    println!("SUM:{} ",sum);

}