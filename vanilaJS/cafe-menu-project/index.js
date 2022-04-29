// STEP1. 요구사항 구현을 위한 전략

// 무조건 개발에 들어가기 보단, 요구 사항을 정확히 분석하는 것으로 시작하자. 기능 구현이라는 '목적'을 분명히!
// 요구 사항을 세부적으로 단위를 나눠 전략을 세우자.
// 한 문장에 하나의 기능이 들어가도록 정리해보자.
// 요구 사항의 순서를 정리하는 것도 좋은 자세이다.

// 기능 구현 완료 후엔 리팩토링을 습관화하기

// ----------------------------------------

// TO DO. 메뉴 추가
// - [V] 메뉴의 이름을 입력받고 확인 버튼을 누르면 메뉴가 추가된다.
// - [V] 메뉴의 이름을 입력받고 엔터키를 누르면 메뉴가 추가된다.
// - [V] 추가되는 메뉴의 마크업은 `<ul id="espresso-menu-list" class="mt-3 pl-0"></ul>` 안에 삽입되어야 한다.
// - [V] 총 메뉴 갯수를 count 하여 상단에 보여준다.
// - [V] 메뉴가 추가되고 나면, input은 빈 값으로 초기화된다.
// - [V] 사용자 입력값이 빈 값이라면 추가되지 않는다.

// TO DO. 메뉴 수정
// 이벤트 위임이라는 개념을 활용한다. 동적으로 추가되는 요소는 부모에게 "이벤트를 위임"한다. <li> 를 추가하기 때문에 상위 부모인 <ul> 태그에 미리 이벤트를 "위임"해둔다.
// - [V] 메뉴 수정 버튼의 클릭 이벤트를 받으면, 메뉴 수정하는 모달이 뜬다.
// - [V] 모달창에 신규 메뉴명을 입력받고, 확인 버튼을 누르면 메뉴가 업데이트된다.

// TO DO. 메뉴 삭제
// - [V] 메뉴 삭제 버튼의 클릭 이벤트를 받으면, 재확인 모달이 뜬다.
// - [V]  확인 버튼 클릭시 메뉴가 삭제된다.
// - [V] 총 메뉴 갯수를 count 하여 상단에 보여준다.

// ----------------------------------------

// localStorage 브라우저 URL 별로 저장되는 저장소.

// TO DO. LocalStorage Read & Write
// - [ ] localStorage에 데이터를 저장한다.
// - [ ] 새로고침해도 localStorage에 있는 데이터를 읽어온다.


// TO DO. 카테고리별 메뉴판 관리
// - [ ] 에스프레소 메뉴가 먼저 보이게 한다.
// - [ ] 에스프레소 메뉴판 관리
// - [ ] 프라푸치노 메뉴판 관리
// - [ ] 블렌디드 메뉴판 관리
// - [ ] 티바나 메뉴판 관리
// - [ ] 디저트 메뉴판 관리

// TO DO. 페이지 접근시 최초 데이터 Read & Rendering
// - [ ] 페이지 최초 로딩시 LocalStorage에 에스프레소 메뉴를 읽어온다.
// - [ ] 에스프레소 메뉴를 페이지에 그려준다.

// TO DO. 품절 상태 관리
// - [ ] 품절 버튼을 추가한다.
// - [ ] 품절 버튼 클릭시 localStorage에 상태값이 저장된다.
// - [ ] 클릭이벤트에서 가장 가까운 li태그의 class 속성 값에 sold-out 을 추가한다.

// ----------------------------------------

// querySelector 가 중복되어 자주 사용되므로, DOM Element 를 가져올때 관용적으로 쓰이는 $ 를 util 로 빼줌
/**
* DOM Element QuerySelector
**/
const $ = selector => document.querySelector(selector);

function App() {
  // 코드를 한 줄 한 줄 읽지 않아도, 함수로 분리해준다면 어떤 기능을 하는 코드인지 쉽게 파악할 수 있다. 몇 달이 지나도 이해할 수 있는 코드를 작성하자.
  const updateMenuCount = () => {
    const menuCount = $("#espresso-menu-list").querySelectorAll("li").length; // 메뉴리스트의 모든 li 갯수
    $(".menu-count").innerText = `총 ${menuCount} 개`;
  };

  const addEspressoMenuItem = () => {
    if ($("#espresso-menu-name").value.replace(/\s/g, "").length == 0) {
      alert("값을 입력해주세요.");
      return;
    }

    const $espressoMenuName = $("#espresso-menu-name").value;

    const menuItemTemplate = espressoMenuName => {
      return `
      <li class="menu-list-item d-flex items-center py-2">
        <span class="w-100 pl-2 menu-name">${espressoMenuName}</span>
        <button
          type="button"
          class="bg-gray-50 text-gray-500 text-sm mr-1 menu-edit-button"
        >
          수정
        </button>
        <button
          type="button"
          class="bg-gray-50 text-gray-500 text-sm menu-remove-button"
        >
          삭제
        </button>
      </li>
    `;
    };
    // $("#espresso-menu-list").innerHTML = menuItemTemplate($espressoMenuName); // 기존값을 덮어쓰게 된다는 문제점.
    $("#espresso-menu-list").insertAdjacentHTML(
      "beforeend",
      menuItemTemplate($espressoMenuName)
    );
    updateMenuCount();
    $("#espresso-menu-name").value = ""; // 입력 후 Input 초기화
  };

  const updateEspressoMenuItem = e => {
    const $menuName = e.target.closest("li").querySelector(".menu-name"); // closest 메서드를 이용해 가까이 있는 Li 태그를 찾을 수 있음.
    const updatedMenuName = prompt("메뉴명을 수정하세요", $menuName.innerText);
    $menuName.innerText = updatedMenuName;
  };

  const removeEspressoMenuItem = e => {
    e.target.closest("li").remove(); // remove : DOM Element 지우는 메서드
    updateMenuCount();
  };

  $("#espresso-menu-list").addEventListener("click", e => {
    // 각 엘레먼트가 가지고 있는 고유값 class 값을 활용
    if (e.target.classList.contains("menu-edit-button")) {
      updateEspressoMenuItem(e);
    }
    if (e.target.classList.contains("menu-remove-button")) {
      if (confirm("정말 삭제하시겠습니까?")) {
        removeEspressoMenuItem(e);
      }
    }
  });

  // form 이 자동으로 전송하는 역할을 하기 때문에 엔터키 입력시 새로고침이 되므로, 이를 막아줘야 한다.
  $("#espresso-menu-form").addEventListener("submit", e => {
    e.preventDefault();
  });

  $("#espresso-menu-submit-button").addEventListener(
    "click",
    addEspressoMenuItem
  );

  $("#espresso-menu-name").addEventListener("keypress", e => {
    if (e.key !== "Enter") {
      return;
    }
    addEspressoMenuItem();
  });
}

App(); // App 함수 실행
