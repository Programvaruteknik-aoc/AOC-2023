use std::collections::HashMap;
use crate::helper::Data;
enum Types {
    RED = 12,
    GREEN = 13,
    BLUE = 14
}
fn get_game_id(){

}
pub fn start(){
    let data = Data::new(2,1);

    let red = 12;
    let green = 13;
    let blue = 14;
    let mut sum = 0;
    for line in data.example.lines(){
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

            games.iter().for_each(|round| {
                println!("\tRound [{}]",round);
                let round:Vec<&str> = round.split(",").map(|v| v.trim()).collect();
                round.iter().for_each(|set| {
                    println!("\t\tSet [{}]",set);
                    let play_str:Vec<&str> = set.split(" ").collect();
                    let mut passed = true;
                    play_str.iter().for_each(|pair|{

                        println!("\t\t\tKey/Value [{}]",pair);
                    });
                });
            });
            // for game in games{
            //     println!("Game {}",game);
            // }
            break;
        }
        // println!("GAME ID:[{}]",game_id);
        // if let Some(game) = first.get(1) {
        //     let mut passed:bool = true;
        //     println!("GAME [{}]",game);
        //     for set in game.split(',').map(|s| s.trim()) {
        //         println!("\tSET [{}]",set);
        //         let pair: Vec<&str> = set.split_whitespace().collect();
        //         if pair.len() == 2 {
        //             print!("\t\tPAIR [");
        //             pair.iter().for_each(|num| print!("{} ", num));
        //             println!("]");
        //             // println!("\tPAIR {}",kv.);
        //
        //             if let (Ok(key), value) = (pair[0].parse::<i32>(), pair[1]) {
        //                 let mut limit = 0;
        //                 if value == "blue"{
        //                     limit = Types::BLUE as i32;
        //                 }
        //                 else if value == "red" {
        //                     limit = Types::RED as i32;
        //                 }
        //                 else if value == "green" {
        //                     limit = Types::GREEN as i32;
        //                 }
        //                 // println!("\tGame {} key:{} value:{} limit:{}",game,key,value,limit);
        //                 if key > limit{
        //                     passed = false;
        //                     break;
        //                 }
        //                 else{
        //
        //                 }
        //
        //                 // println!("Key: {}, Value: {}", key, value);
        //             }
        //         }
        //     }
        //     // Add sum
        //     if passed {
        //         sum += game_id;
        //     }
        // }
    }

    println!("SUM:{} ",sum);

}