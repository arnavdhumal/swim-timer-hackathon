function select_sport() {
    var sportvalue = document.getElementById("sport").value;
    if (sportvalue == "Swimming") {
        document.getElementById("swim_form").style = 'block';
    }
}
function start() {
    console.log("start")
};
function lap() {
    console.log("lap")
};
function stop() {
    console.log("stop")
};
/*document.getElementById("start").addEventListener("click", function() {
    console.log("start")
});
document.getElementById("lap").addEventListener("click", function() {
    console.log("lap")
});
document.getElementById("end").addEventListener("click", function() {
    console.log("start")
});*/
