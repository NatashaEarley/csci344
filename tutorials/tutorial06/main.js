// Part 1: Set up the helper functions:
// 1. Implement two filter functions (which should return either true or false):
//      * filterClassFull: to filter out the closed courses (if applicable)
//      * filterTermMatched: to only match courses relevant to the search term
// 2. Implement the dataToHTML function, which takes a course object as an
//    argument and returns an HTML string that represents the course.

// Part 2: Within the showData function, use the array's filter, map, join
//         methods, and any relevant DOM methods, to build the interface.
// 1. Use the array's built in "filter" method, which takes a filter
//    function as an argument and returns an array of objects that
//    match the criteria.
//          * Note that you can chain filter functions together.
// 2. Use the array's built in "map" method to generate an array of
//    HTML strings.
// 3. Join the array of strings on the empty string or new line character
//    to create one large HTML string.
// 4. Clear out the existing courses in the DOM and insert
//    the HTML string into the DOM.

const search = (ev) => {
    ev.preventDefault(); // overrides default button action

    // Get user's preferences:
    const searchTerm = document.querySelector("#search_term").value;
    const openOnly = document.querySelector("#is_open").checked;

    // Pass the user's preferences into the showData function
    showData(searchTerm, openOnly);
};

// Part 1.1b
const filterTermMatched = (course) => {
    // modify this
    return true;
};

// Part 1.2
const dataToHTML = (course) => {
    return `
        <section class="course">
            <h2>${course.Code}: ${course.Title}</h2>
            <p>
                ${checkOrEx(course)} ${openOrClosed(course)}  &bull; ${course.CRN} &bull; Seats Available: ${calcSeats(course)}
            </p>
            <p>
                ${ showDays(course) }
                ${course.Location.FullLocation || ""} &bull; 
                ${course.Hours} credit hour(s)
            </p>
            <p><strong>${course.Instructors[0].Name}</strong></p>
        </section>
    `;
};

const checkOrEx = (course) => {
    if (course.Classification.Open === true) {
        return `<i class="fa-solid fa-circle-check"></i>`
    } else {
        return `<i class="fa-solid fa-circle-xmark"></i>`
    }
}

const openOrClosed = (course) => {
    if (course.Classification.Open === true) {
        return `Open`
    } else {
        return `Closed`
    }
}

const calcSeats = (course) => {
    let a = `${course.EnrollmentCurrent}`;
    let b = `${course.EnrollmentMax}`;
    let result = b - a;
    return result;
}

const showDays = (course) => {
    if (course.Days) {
        return `${course.Days} &bull; `;
    }
    return "";
};

const addCourseToDOM = (course) => {
    const htmlSnippet = dataToHTML(course);
    const containerEL = document.querySelector(".courses");
    containerEL.innerHTML += htmlSnippet;
}

// Part 2
const showData = (searchTerm, openOnly) => {
    console.log(searchTerm, openOnly);
    console.log(data);

    const searchTermMatch = (course) => {
        return course.Title.toLowerCase().includes(searchTerm.toLowerCase());
    };

    const filterByOpen = (course) => {
        return !openOnly || course.Classification.Open;
    };

    const filterClassFull = (course) => {
        let seatsAvailable = calcSeats(course);
        return seatsAvailable > 0;
    };

    const filterClassChecked = document.getElementById("is_open").checked;

    document.querySelector(".courses").innerHTML = "";
    data
        .filter(course => 
            searchTermMatch(course) && 
            filterByOpen(course) && 
            (!filterClassChecked || filterClassFull(course))
        )
        .forEach(addCourseToDOM);
};

// I used ChatGPT for creating filterByOpen and filterClassFull and how to impliment them into the DOM