package com.hbaseeye.controller;

import com.hbaseeye.model.MasterInfo;
import com.hbaseeye.service.HMasterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/8.
 */
@Controller
@RequestMapping("/")
public class HMasterController {

    @Autowired
    private HMasterService hMasterService;

    @RequestMapping(value = "/hmaster", method = RequestMethod.GET)
    public ModelAndView hMaster(HttpServletRequest request){
        ModelAndView modelAndView = new ModelAndView("hmaster");

        List<MasterInfo> masterInfo = hMasterService.getMasterInfo();
        modelAndView.addObject("hmasterinfo", masterInfo);
        return modelAndView;
    }
}
