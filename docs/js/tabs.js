let tabsWithContent = (function () {
  let tops = document.querySelectorAll('.tabs-with-content')
  tops.forEach(function (twc) {
    let tabs = twc.querySelectorAll('.tabs li');
    let tabsContent = twc.querySelectorAll('.tab-content');

    let deactvateAllTabs = function () {
      tabs.forEach(function (tab) {
        tab.classList.remove('is-active');
      });
    };

    let hideTabsContent = function () {
      tabsContent.forEach(function (tabContent) {
        tabContent.classList.remove('is-active');
      });
    };

    let activateTabsContent = function (tab) {
      tabsContent[getIndex(tab)].classList.add('is-active');
    };

    let getIndex = function (el) {
      return [...el.parentElement.children].indexOf(el);
    };

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        deactvateAllTabs();
        hideTabsContent();
        tab.classList.add('is-active');
        activateTabsContent(tab);
      });
    })

    tabs[0].click();

  })
})();
