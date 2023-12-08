use std::collections::HashMap;
use std::sync::mpsc::channel;
use crate::helper::Data;
fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let t = b;
        b = a % b;
        a = t;
    }
    a
}

fn lcm(a: u64, b: u64) -> u64 {
    a / gcd(a, b) * b // The order of operations is important to avoid overflow
}
pub fn start(){
    let data:Data = Data::new(8,2);
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

    let mut steps:u64 = 1;
    let mut cycle_iter = (0..directions.len()).cycle();
    nodes.iter().for_each(|node|{
        let mut c = directions.chars().nth(0).unwrap();
        if node.0.ends_with('A'){
            let mut count:u64 = 0;
            let mut res:&str = node.0;
            while !res.ends_with('Z') {
                c = directions.chars().nth(cycle_iter.next().unwrap()).unwrap();
                let map = nodes.get(res).unwrap();
                res = if c=='R' { &map.1 }else { &map.0 };
                count += 1;
            }
            steps = lcm(steps,count);
        }
    });
    println!("Steps:{}",steps);

}
