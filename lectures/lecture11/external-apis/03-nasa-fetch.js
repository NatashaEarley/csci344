const getMeteors = async (startDate, endDate) => {
    const rootURL = "https://api.nasa.gov/neo/rest/v1/feed";
    const apiKey = "Nkm2F2D17dlqJlgMgpodpiFiL0rNgecSNa6cZKYu";
    const endpoint = `${rootURL}?api_key=${apiKey}&start_date=${startDate}&end_date=${endDate}`;
    const response = await fetch(endpoint);
    const jsonData = await response.json();
    return jsonData;
};

// meteors
const data = await getMeteors("2024-10-08", "2024-10-09");
console.log(data);

/**
 * Exercise:
 *      1. How would I access all of the meteors from '2024-10-08'?
 *      2. How would I print all the names of all the meteors?
 *
 */





// Answers:
// 1. all of the meteors from '2024-10-08'
// console.log(data.near_earth_objects["2024-10-08"]);

// 2. output all meteor names
// create a list of all of the meteors:
// let meteorList = [];
// for (const key in data.near_earth_objects) {
//     meteorList = meteorList.concat(data.near_earth_objects[key]);
// }
// meteorList.forEach((meteor) => console.log(meteor.name));
