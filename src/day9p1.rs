use std::process::exit;
pub use crate::helper::Data;

struct Holder{
    pub numbers:Vec<i64>,
    pub steps:Vec<i64>,
    pub sub_steps:Vec<i64>
}

impl Holder {
    pub fn new() -> Holder{
        Holder{ numbers: vec![], steps: vec![], sub_steps: vec![] }
    }
}
fn find_missing(){

}
fn find_steps(mut container: &mut Vec<Vec<i64>>) -> i64{
    if container.last().unwrap().iter().all(|&x| x == 0){
        //println!("Cont len{}",container.len());
        let mut last:i64 = 0;
        let mut first:bool = true;
        container.iter_mut().rev().for_each(|step|{
            let a:i64 = *step.last().unwrap();
            let nv = a+last;

            //println!("{} {} {}",a,last,nv);
            //println!("New Value:{}",nv);
            step.push(nv);
            last = nv;
        });
            //println!("NV:{}",last);
        for steps in container {
            for step in steps {
                print!("{} ",step);
            }
            println!();
        }
        return 0
    }
    let mut steps:Vec<i64> = Vec::new();
    for index in 1..container.last().unwrap().len(){
        let num:i64 = *container.last().unwrap().get(index).unwrap() - *container.last().unwrap().get(index-1).unwrap();
        steps.push(num);
    }
    container.push(steps);
    let cock =find_steps(container);
    return 0;
}



pub fn start(){
    let data:Data = Data::new(9,1);
    let mut sum:i64 = 0;

    data.input.lines().for_each(|line| {
    let mut container: Vec<Vec<i64>> = Vec::new();
        let seed: Vec<i64> = line.split_whitespace()
            .map(|number| number.parse::<i64>().unwrap())
            .collect();
        container.push(seed);
        find_steps(&mut container);
        let res = container.first().unwrap().last().unwrap();
        sum += res;
        println!("{}",res);
        println!("*****************************************************************************************");
    });
    // container.iter().for_each(|step|{
    //     step.iter().for_each(|v|{
    //         //println!("{} ",v);
    //     });
    // });
    // container.iter().for_each(|step|{
    //     step.iter().for_each(|v| {
    //         print!("{} ", v);
    //         });
    //     println!("*******************");
    // });
    //
    // let num = *container.last().unwrap().first().unwrap();
    // println!("len:{}",container.first().unwrap().len());
    // println!("num:{}",num);
    // sum += *container.last().unwrap().first().unwrap();
    println!("Sum:{}",sum);
    // sum += *container.last().unwrap().last().unwrap();
}