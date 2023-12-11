use std::any::type_name;
use std::cell::RefCell;
use std::collections::HashMap;
use std::io::Chain;
use std::ptr::null;
use std::rc::Rc;
use crate::day9p1::Data;

struct Node {
    parent: Option<Rc<RefCell<Node>>>,
    coord: (i64, i64),
    pipe: char,
    children: Vec<Rc<RefCell<Node>>>,
    step:u64
}



fn find_children_for_node<'a>(cells:&HashMap<(i64,i64),char>, nodes: &mut Vec<Rc<RefCell<Node>>>, consumed: &mut Vec<(i64, i64)>, node: &Rc<RefCell<Node>>){
    let mut exits:Vec<(i64,i64)>;
    //let mut consumed:Vec<(i64,i64)> = vec![];
    let pipe = node.borrow_mut().pipe;
    let cur = node.borrow_mut().coord;
    let n:(i64,i64) = (cur.0, cur.1-1);
    let s:(i64,i64) = (cur.0, cur.1+1);
    let w:(i64,i64) = (cur.0-1, cur.1);
    let e:(i64,i64) = (cur.0+1, cur.1);
    match pipe {
        '|' => { exits = vec![n,s] }
        '-' => { exits = vec![w,e] }
        'L' => { exits = vec![n,e] }
        'J' => { exits = vec![n,w] }
        '7' => { exits = vec![s,w] }
        'F' => { exits = vec![s,e] }
        //'.' => { exits = node.children.extend(vec![] }

        _ => {exits = vec![]}
    }
    for exit in exits {
        if *cells.get(&exit).unwrap() != '.' && !consumed.contains(&exit){
            //let mut ch_node:Node = Node::new(Some(node.clone()), exit, *cells.get(&exit).unwrap());
            let child = Rc::new(RefCell::new(Node{
                parent:Some(Rc::clone(&node)),
                coord:exit,
                pipe:*cells.get(&exit).unwrap(),
                children:vec![],
                step:node.borrow().step + 1
            }));
            node.borrow_mut().children.push(Rc::clone(&child));
            nodes.push(child);
            consumed.push(exit);
        }
    }

    //consumed
}
fn get_exits_for_pipe(pipe:char) -> Vec<char>{
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
    exits
}
fn get_exit_coords(node: &mut Node) -> Vec<(i64,i64)>{
    let cur = node.coord;
    let c = node.pipe;
    let mut exit_cords:Vec<(i64,i64)> = vec![];
    let exits = get_exits_for_pipe(c);
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
        if get_exits_for_pipe(*s.unwrap()).contains(&'N') {
            exits.push('S');
        }
    }
    if n.is_some() {
        if get_exits_for_pipe(*n.unwrap()).contains(&'S') {
            exits.push('N');
        }
    }
    if w.is_some() {
        if get_exits_for_pipe(*w.unwrap()).contains(&'E') {
            exits.push('W');
        }
    }
    if e.is_some(){
        if get_exits_for_pipe(*e.unwrap()).contains(&'W'){
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
    let mut nodes:Vec<Rc<RefCell<Node>>> = vec![];
    let mut start:Vec<(i64,i64)> = vec![];

    data.input.lines().enumerate().for_each(|line|{
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

    //let mut node = Node::new(None,*s,p);
    let root = Rc::new(RefCell::new(Node{
        parent: None,
        coord:*s,
        pipe:p,
        children:vec![],
        step:0
    }));
    //let cons = find_children_for_node(&cells, &mut nodes, &mut consumed, &root);

    let mut current_nodes:Vec<Rc<RefCell<Node>>> = vec![root];
    let mut next_nodes:Vec<Rc<RefCell<Node>>> = vec![];
    while current_nodes.len() > 0 {
        for child in current_nodes.iter() {
            find_children_for_node(&cells, &mut nodes, &mut consumed, child);

            let child_rc = Rc::clone(child); // Clone the Rc
            let child_children = child_rc.borrow().children.clone(); // Clone the children
            next_nodes.extend(child_children); // Extend with the owned cloned children
        }

        current_nodes.clear();
        current_nodes.extend(next_nodes.clone());
        next_nodes.clear();

    }
    let max = nodes.iter().max_by_key(|node|node.borrow().step).unwrap().borrow().step;
    println!("Step:{}",max);

    // for child in current_node.borrow_mut().children.iter() {
    //     find_children_for_node(&cells, &mut nodes, &mut consumed,&child);
    // }
    //
    // for child in root.borrow_mut().children.iter() {
    //     let pipe = child.borrow().pipe; // Use borrow() if you don't need to mutate child
    //     println!("Pipe: {}", pipe);
    // }
    // for con in consumed {
    //     println!("x{} : y{}",con.0,con.1);
    // }
}