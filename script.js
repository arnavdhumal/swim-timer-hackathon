let start_time;
let end_time;
function select_swim() {
    document.getElementById("swim_form").style = 'block';
}
function start() {
    // console.log("start")
    const x = new Date();
    start_time = x.getTime();
    console.log(start_time)
};
function lap() {
    // console.log("lap")
};
function stop() {
    // console.log("stop")
    const y = new Date();
    end_time = y.getTime();
    total_time = getTotalTime();
    total_time_seconds = total_time / 1000;
    console.log(end_time)
    console.log(total_time_seconds);
    let output = "Total Time: " + total_time_seconds + " seconds"
    var result = document.getElementById("result");
    result.innerHTML = output;
    console.log(output)
};
function getTotalTime() {
    var total_time = end_time - start_time;
    return total_time;
}

function save() {
    var event = {
        name: document.getElementById('name').value,
        sport: document.getElementById("sport").value,
        length: document.getElementById("pool_length").value,
        sport_type: document.querySelector('input[name="stroke"]:checked').value,
        total_time: total_time_seconds
    };
    console.log(event)
}

