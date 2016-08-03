/*
 * This is a JavaScript Scratchpad.
 * No, this is Patric
 */
var dateregex = /([0-9]?[0-9])[-\/]((?:[0-9]?[0-9])?(?:[a-zA-Z]*)?)[-\/]?([0-9]{0,4})/g;
var timeregex = /([0-9]?[0-9]):([0-9]?[0-9])\s*([aApP]\.?[mM])?/g;
if (window.getSelection) {
    var sel = window.getSelection();
    if (sel.rangeCount) {
        sel = sel.toString();
        console.log(sel);
        var date = dateregex.exec(sel);
        var time = timeregex.exec(sel);
        if (time[0])
            time[0].replace('.', '');
        if (time[3])
            time[3].replace('.', '');
        console.log(date, time);
    }
}