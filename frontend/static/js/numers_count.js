// document.addEventListener('DOMContentLoaded', () => {
//     const counters = document.querySelectorAll('.counter .number');

//     counters.forEach(counter => {
//         counter.innerText = '0';
//         const updateCounter = () => {
//             // Pobierz wartość docelową
//             const target = +counter.parentElement.getAttribute('data-target');
//             // Pobierz aktualną wartość licznika
//             const c = +counter.innerText;

//             // Oblicz krok
//             const increment = target / 200; // Im mniejsza wartość, tym wolniejsza animacja

//             // Jeśli aktualna wartość jest mniejsza od docelowej, kontynuuj liczenie
//             if(c < target) {
//                 // Zaokrągl w górę i zaktualizuj licznik w HTML
//                 counter.innerText = `${Math.ceil(c + increment)}`;
//                 // Wywołaj funkcję ponownie po krótkiej przerwie
//                 setTimeout(updateCounter, 1);
//             } else {
//                 // Jeśli osiągnięto wartość docelową, upewnij się, że wyświetlana jest dokładna liczba
//                 counter.innerText = target;
//             }
//         };

//         // Uruchom animację
//         updateCounter();
//     });
// });