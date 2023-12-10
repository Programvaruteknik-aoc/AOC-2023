use std::any::type_name;
use std::collections::HashMap;
use std::io::Chain;
use std::ptr::null;
use crate::day9p1::Data;


struct Node<'a> {
    parent: Option<&'a Node<'a>>,
    coord: (i64, i64),
    pipe: char,
    children: Vec<Node<'a>>,
}

impl<'a> Node<'a> {
    pub fn new(parent: Option<&'a Node<'a>>, coord: (i64, i64), pipe: char) -> Node<'a> {
        Node {
            parent,
            coord,
            pipe,
            children: Vec::new(),
        }
    }
}
fn find_children_for_pipe(node:Node) -> Vec<(i64,i64)>{
    let mut exits:Vec<char>;
    match pipe {
        '|' => { exits = vec!['N','S'] }
        '-' => { exits = vec!['W','E'] }
        'L' => { exits = vec!['N','E'] }
        'J' => { exits = vec!['N','W'] }
        '7' => { exits = vec!['S','W'] }
        'F' => { exits = vec!['S','E'] }
        '.' => { exits = vec![] }

        _ => {exits = vec![]}
    }
    exits.iter().filter(|&&exit| exit != enter).map(|&exit| exit).collect()
}
fn get_exits(enter:char, pipe:char) -> Vec<char>{
    let mut exits:Vec<char>;
    match pipe {
        '|' => { exits = vec!['N','S'] }
        '-' => { exits = vec!['W','E'] }
        'L' => { exits = vec!['N','E'] }
        'J' => { exits = vec!['N','W'] }
        '7' => { exits = vec!['S','W'] }
        'F' => { exits = vec!['S','E'] }
        '.' => { exits = vec![] }

        _ => {exits = vec![]}
    }
    exits.iter().filter(|&&exit| exit != enter).map(|&exit| exit).collect()
}
fn get_exit_coords(node: &mut Node) -> Vec<(i64,i64)>{
    let cur = node.coord;
    let c = node.pipe;
    let mut exit_cords:Vec<(i64,i64)> = vec![];
    let exits = get_exits('X',c);
    let n:(i64,i64) = (cur.0, cur.1-1);
    let s:(i64,i64) = (cur.0, cur.1+1);
    let w:(i64,i64) = (cur.0-1, cur.1);
    let e:(i64,i64) = (cur.0+1, cur.1);
    if exits.contains(&'N'){ exit_cords.push(n);}
    if exits.contains(&'S'){ exit_cords.push(s);}
    if exits.contains(&'W'){ exit_cords.push(w);}
    if exits.contains(&'E'){ exit_cords.push(e);}
    exit_cords
}
fn find_start_pipe(cells:&HashMap<(i64,i64),char>, coord:(i64,i64)) -> char {
    let mut exits:Vec<char> = vec![];
    let n = cells.get(&(coord.0, coord.1 - 1));
    let s = cells.get(&(coord.0, coord.1 + 1));
    let w = cells.get(&(coord.0 - 1, coord.1));
    let e = cells.get(&(coord.0 + 1, coord.1));
    if s.is_some() {
        if get_exits('X', *s.unwrap()).contains(&'N') {
            exits.push('S');
        }
    }
    if n.is_some() {
        if get_exits('X', *n.unwrap()).contains(&'S') {
            exits.push('N');
        }
    }
    if w.is_some() {
        if get_exits('X', *w.unwrap()).contains(&'E') {
            exits.push('W');
        }
    }
    if e.is_some(){
        if get_exits('X',*e.unwrap()).contains(&'W'){
            exits.push('E');
        }
    }
    if exits.contains(&'N') && exits.contains(&'S') { return '|'; }
    else if exits.contains(&'W') && exits.contains(&'E') { return '-'; }
    else if exits.contains(&'N') && exits.contains(&'E') { return 'L'; }
    else if exits.contains(&'N') && exits.contains(&'W') { return 'J'; }
    else if exits.contains(&'S') && exits.contains(&'W') { return '7'; }
    else if exits.contains(&'S') && exits.contains(&'E') { return 'F'; }
    return 'X';
}
pub fn start(){
    let data:Data = Data::new(10,1);
    let mut cells:HashMap<(i64,i64),char> = HashMap::new();
    let mut consumed:Vec<(i64,i64)> = Vec::new();
    let mut start:Vec<(i64,i64)> = vec![];
    data.example.lines().enumerate().for_each(|line|{
        //println!("{}",line.1);
        let y = line.0 as i64;
        let s = line.1;
        s.chars().enumerate().for_each(|ch|{
            let x = ch.0 as i64;
            let c = ch.1;
            cells.insert((x,y),c);
            if c == 'S' {
                start.push((x,y));
            }
        })
    });
    let s = start.first().unwrap();
    let p = find_start_pipe(&cells,*s);

    let mut node = Node::new(None,*s,p);
    consumed.push(node.coord);
    let children:Vec<(i64,i64)> = get_exit_coords(&mut node);
    for child in children {
        if !consumed.contains(&child){
            let mut ch_node:Node = Node::new(Some(&node),child,*cells.get(&child).unwrap());
            //node.children.push(ch_node);
        }
    }
    println!("P:{}",p);
    for child in children {
        println!("Child:{}",cells.get(&child).unwrap());
    }
    //let start_node = Node::new(*s, p);
    //

    // for dir in s_dir {
    //     println!("Start direction:{}",dir)
    // }
    //
    // for dir in s_dir {
    //     let mut steps = 0;
    //     let cur = s;
    //     let heading:(i64,i64);
    //     while cells.get(&cur).unwrap() != '.' {
    //
    //     }
    //     match dir {
    //         'N' => { heading = (s.0, s.1 - 1) }
    //         'S' => { heading = (s.0, s.1 + 1) }
    //         'W' => { heading = (s.0 - 1, s.1) }
    //         'E' => { heading = (s.0 + 1, s.1) }
    //         _ => {}
    //     }
    // }
}