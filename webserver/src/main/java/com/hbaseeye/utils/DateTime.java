package com.hbaseeye.utils;


import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import static java.util.Calendar.MINUTE;

/**
 * Created by yuanxiaobin on 16/12/14.
 */
public class DateTime {
    public String getTimeStr(int hour){
        Calendar calendar = Calendar.getInstance();
        calendar.add(MINUTE, -hour);
        String str = (new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")).format(calendar.getTime());

        return str;
    }

    public Long getMSTime(String strTime){
        Long time = null;
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        try {
            Calendar calendar = Calendar.getInstance();
            Date date = dateFormat.parse(strTime);
            calendar.setTime(date);
            time = calendar.getTimeInMillis();

        } catch (ParseException e) {
            e.printStackTrace();
        }

        return time;

    }
}
