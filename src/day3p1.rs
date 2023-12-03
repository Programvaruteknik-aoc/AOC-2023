use std::sync::mpsc::sync_channel;
use crate::day1_1::is_digit;
use crate::helper::Data;

fn validate_cell(pos:(i32,i32), xlimit:i32, ylimit:i32) -> Option<(i32,i32)> {
    if pos.0 >= 0 && pos.1 >= 0 && pos.0 < xlimit as i32 && pos.1 < ylimit as i32 {
         return Some(pos);
     }
    None
}

fn neighbours(pos: (i32, i32), xlimit: i32, ylimit:i32) -> Vec<(i32, i32)> {
    let mut nb: Vec<(i32, i32)> = Vec::new();
    nb.push((pos.0 - 1, pos.1 - 1));
    nb.push((pos.0 - 1, pos.1));
    nb.push((pos.0 - 1, pos.1 + 1));

    nb.push((pos.0 + 1, pos.1 - 1));
    nb.push((pos.0 + 1, pos.1));
    nb.push((pos.0 + 1, pos.1 + 1));

    nb.push((pos.0, pos.1 - 1));
    nb.push((pos.0, pos.1 + 1));

    nb.into_iter()
        .filter(|dolk| validate_cell(*dolk, xlimit, ylimit).is_some())
        .collect()
}

    fn who_dis(data:&Data) -> String {
        let mut symbols:String = String::from("");
        data.input.lines().for_each(|line|{
            line.chars().enumerate().for_each(|c|{
                if is_digit(c.1) || c.1 == '.' {

                }
                else {
                    if !symbols.contains(c.1){
                        symbols = format!("{}{}",symbols,c.1);
                    }
                }
            })
        });
        symbols
    }

pub fn start(){

    let data : Data = Data::new(3,1);
    // let symbols = "!#$%&'*+,-()";
    let symbols = who_dis(&data);
    let mut sum:u32 = 0;
    let mut start:u32 = 0;
    let mut v:u32 = 0;
    let mut word:String = String::from("");
    let mut line_num = 0;
    let mut has_pn = false;
    let mut lines:Vec<&str> = data.input.lines().collect();
    let lines_count = lines.len() as i32;
    data.input.lines().for_each(|line|{
        let mut pre:char = char::from(0);
        line.chars().enumerate().for_each(|ch|{
            let c = ch.1;
            let i = ch.0;

            if is_digit(c){
                if is_digit(pre){
                    // First digit
                    word = format!("{}{}",word,c);

                }
                else{
                    // Second, third .... digit
                    word = String::from(c);
                }
                let cord:(i32,i32) = (i as i32,line_num);
                let neighbours = neighbours(cord, line.len() as i32, lines_count);
                neighbours.iter().for_each(|cell|{
                    let row:&str = lines.get(cell.1 as usize).unwrap();
                    let col:char = row.chars().nth(cell.0 as usize).unwrap();
                    if symbols.contains(col){
                        has_pn = true;
                    }
                });
            }
            else {
                // If not on digit
                if is_digit(pre) {
                    v = word.parse().unwrap();
                    println!("[{}] \t{}",v,has_pn);
                    has_pn = false;
                    sum += v;
                }
                else{

                }
            }
            pre = c;
        });
        line_num += 1;
    });
    println!("SYMBOLS:[{}]",symbols);
    println!("SUM:{}",sum);
}