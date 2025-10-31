
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Smart Calendar</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: "Poppins", sans-serif;
    }

    body {
      background: linear-gradient(135deg, #0099ff, #6610f2);
      color: #fff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .calendar {
      width: 95%;
      max-width: 420px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(12px);
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }

    .calendar header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 1.4em;
      font-weight: 600;
      margin-bottom: 10px;
    }

    .calendar button {
      background: rgba(255,255,255,0.2);
      border: none;
      color: #fff;
      font-size: 1.3em;
      border-radius: 10px;
      padding: 5px 10px;
      cursor: pointer;
      transition: 0.2s;
    }

    .calendar button:hover {
      background: rgba(255,255,255,0.3);
    }

    .days {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 5px;
      margin-top: 10px;
    }

    .day {
      text-align: center;
      padding: 10px 0;
      border-radius: 10px;
      transition: 0.2s;
    }

    .day:hover {
      background: rgba(255,255,255,0.2);
    }

    .today {
      background: #ff4081;
    }

    .weekdays {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      font-weight: 600;
      margin-bottom: 5px;
    }

    footer {
      margin-top: 15px;
      font-size: 0.9em;
      opacity: 0.8;
    }
  </style>
</head>
<body>
  <div class="calendar">
    <header>
      <button id="prev">&#10094;</button>
      <div id="month-year"></div>
      <button id="next">&#10095;</button>
    </header>
    <div class="weekdays">
      <div>রবি</div><div>সোম</div><div>মঙ্গল</div><div>বুধ</div><div>বৃহস্পতি</div><div>শুক্র</div><div>শনি</div>
    </div>
    <div class="days" id="days"></div>
  </div>

  <footer>© 2025 Smart Calendar</footer>

  <script>
    const monthYear = document.getElementById("month-year");
    const daysContainer = document.getElementById("days");
    const prevBtn = document.getElementById("prev");
    const nextBtn = document.getElementById("next");

    let date = new Date();

    function renderCalendar() {
      const year = date.getFullYear();
      const month = date.getMonth();
      const today = new Date();

      const firstDay = new Date(year, month, 1).getDay();
      const lastDate = new Date(year, month + 1, 0).getDate();

      const monthNames = [
        "জানুয়ারি","ফেব্রুয়ারি","মার্চ","এপ্রিল","মে","জুন",
        "জুলাই","আগস্ট","সেপ্টেম্বর","অক্টোবর","নভেম্বর","ডিসেম্বর"
      ];

      monthYear.textContent = `${monthNames[month]} ${year}`;

      daysContainer.innerHTML = "";

      for (let i = 0; i < firstDay; i++) {
        const empty = document.createElement("div");
        daysContainer.appendChild(empty);
      }

      for (let day = 1; day <= lastDate; day++) {
        const dayEl = document.createElement("div");
        dayEl.classList.add("day");
        dayEl.textContent = day;

        if (
          day === today.getDate() &&
          month === today.getMonth() &&
          year === today.getFullYear()
        ) {
          dayEl.classList.add("today");
        }

        daysContainer.appendChild(dayEl);
      }
    }

    prevBtn.onclick = () => {
      date.setMonth(date.getMonth() - 1);
      renderCalendar();
    };

    nextBtn.onclick = () => {
      date.setMonth(date.getMonth() + 1);
      renderCalendar();
    };

    renderCalendar();
  </script><img width="840" height="859" alt="calendar-icon-png-image-download-schedule-ico-11563017254aqqdsuczph" src="https://github.com/user-attachments/assets/90c410ab-2ff9-471e-abe2-8a9e9b30a307" />
<img width="704" height="1472" alt="1761897295050" src="https://github.com/user-attachments/assets/a0f29fba-9cdc-4f6d-9f72-46f52b09516e" />

</body>
</html>
