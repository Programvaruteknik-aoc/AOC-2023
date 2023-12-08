use std::collections::HashMap;
use std::sync::mpsc::channel;
use crate::helper::Data;

pub fn start(){
    let data:Data = Data::new(8,1);
    let mut directions = "";
    let mut nodes:HashMap<&str,(&str,&str)> = HashMap::new();
    for line in data.input.lines().enumerate() {
        if(line.0 == 0){
            directions = line.1;
        }
        else if line.0 > 1{
            let tup:(&str,&str) = line.1.split_once(" = (").unwrap();
            let key = tup.0;
            let tup2 = tup.1.split_once(", ").unwrap();
            nodes.insert(key,(tup2.0,&tup2.1[..3]));
        }
    }
    // for (key,value) in nodes{
    //
    //     println!("Key:{} Value:{:?}",key,value);
    // }

    let mut res = "AAA";
    let mut run = true;
    let mut index = 0;
    let mut steps = 0;
    while run == true {
        if index == directions.len(){
           index = 0;
        }
        let c = directions.chars().nth(index).unwrap();
        //let dir = if c == 'R' {1} else { 0 };
        let tup = nodes.get(res).unwrap();
        println!("Index:{}",index);
        res = if c == 'R' { tup.1 } else { tup.0 };
        if res == "ZZZ" {
            println!("Steps:{}",steps +1 );
            run = false;
        }
        index += 1;
        steps += 1;
    }
}
