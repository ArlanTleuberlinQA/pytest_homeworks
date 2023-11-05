import pytest


@pytest.mark.regression_cases
def test_change_season(open_serial_page):
    ser_page = open_serial_page
    ser_page.change_season_to_2()
    assert ser_page.is_season_changed(), "Season doesn't changed"


@pytest.mark.regression_cases
def test_change_dub(open_serial_page):
    ser_page = open_serial_page
    ser_page.change_dub_to_ukr()
    assert ser_page.is_dub_changed(), "Dub doesn't changed"


@pytest.mark.smoke_cases
def test_ads_show(open_serial_page):
    ser_page = open_serial_page
    ser_page.play_video()
    assert ser_page.is_ads_appear(), "ADS doesn't showed"


@pytest.mark.smoke_cases
def test_video_playing(open_serial_page):
    ser_page = open_serial_page
    ser_page.play_video()
    ser_page.wait_till_ads_disappear()
    assert ser_page.is_timecode_appear(), "Video doesn't playing"


@pytest.mark.regression_cases
def test_trailer_autoplay(open_serial_page):
    ser_page = open_serial_page
    ser_page.play_trailer()
    assert ser_page.is_trailer_autoplay(), "Trailer doesn't autoplaying"
