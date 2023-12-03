use crate::helper::Data;

fn validate_cell(pos:(i32,i32), xlimit:i32, ylimit:i32) -> Option<(i32,i32)> {
    if pos.0 >= 0 && pos.1 >= 0 && pos.0 < xlimit && pos.1 < ylimit{
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
                if c.1 >= '0' && c.1 <= '9' || c.1 == '.' {

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
    println!("SYMBOLS:{}",symbols);
    let mut sum:u32 = 0;
    let mut start:i64 = -1;
    let mut v:i32 = 0;
    let mut word:String = String::from("");
    let mut line_num = 0;
    let mut has_pn = false;
    let mut lines:Vec<&str> = data.input.lines().collect();
    let lines_count = lines.len() as i32;
    data.input.lines().for_each(|line|{
        line.chars().enumerate().for_each(|c|{
            if c.1 == '.' && start != -1{
                println!("Number [{}]",word);
                v = word.parse::<i32>().unwrap();
                if has_pn {
                    sum += v as u32;
                }

                word = String::from("");
                start = -1;
                has_pn = false;
            }
            if c.1 >= '0' && c.1 <= '9' {
                if(start == -1){
                    start = c.0 as i64;
                }
                word = format!("{}{}",word,c.1);

                let cord:(i32,i32) = (c.0 as i32,line_num);
                let neighbours = neighbours(cord, line.len() as i32, lines_count);
                // println!("{}  *********************************",neighbours.len());

                neighbours.iter().for_each(|coord|{
                    let l:&str = lines.get(coord.1 as usize).unwrap();
                    let c:char = l.chars().nth(coord.0 as usize).unwrap();
                    // print!("[{}]",c);
                    if symbols.contains(c){
                        has_pn = true;
                    }
                })
            }

        });
        line_num += 1;
    });
    println!("SUM:{}",sum);
}