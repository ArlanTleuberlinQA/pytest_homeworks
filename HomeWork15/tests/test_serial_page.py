import pytest
import allure


@pytest.mark.ui
@allure.story("Test changing season")
@allure.title("Verify season change")
@allure.description("This test verifies the ability to change the season on the serial page.")
@allure.tag("Serial Page", "Season")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_change_season(open_serial_page):
    ser_page = open_serial_page
    ser_page.change_season_to_2()
    assert ser_page.is_season_changed(), "Season doesn't changed"


@pytest.mark.ui
@allure.story("Test changing dub")
@allure.title("Verify dub change")
@allure.description("This test verifies the ability to change the dub on the serial page.")
@allure.tag("Serial Page", "Dub")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_change_dub(open_serial_page):
    ser_page = open_serial_page
    ser_page.change_dub_to_ukr()
    assert ser_page.is_dub_changed(), "Dub doesn't changed"


@pytest.mark.ui
@allure.story("Test ADS display")
@allure.title("Verify ADS display")
@allure.description("This test verifies the display of ADS on the serial page.")
@allure.tag("Serial Page", "ADS")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_ads_show(open_serial_page):
    ser_page = open_serial_page
    ser_page.play_video()
    assert ser_page.is_ads_appear(), "ADS doesn't showed"


@pytest.mark.ui
@pytest.mark.smoke_cases
def test_video_playing(open_serial_page):
    ser_page = open_serial_page
    ser_page.play_video()
    ser_page.wait_till_ads_disappear()
    assert ser_page.is_timecode_appear(), "Video doesn't playing"


@pytest.mark.ui
@allure.story("Test trailer autoplay")
@allure.title("Verify trailer autoplay")
@allure.description("This test verifies the autoplay of the trailer on the serial page.")
@allure.tag("Serial Page", "Trailer")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_trailer_autoplay(open_serial_page):
    ser_page = open_serial_page
    ser_page.play_trailer()
    assert ser_page.is_trailer_autoplay(), "Trailer doesn't autoplaying"
