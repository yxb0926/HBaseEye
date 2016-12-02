package com.hbaseeye;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.context.web.SpringBootServletInitializer;
import org.springframework.stereotype.Controller;

/**
 * Created by yxb on 16/12/1.
 */

@Controller
@EnableAutoConfiguration
@SpringBootApplication
public class EyeApp extends SpringBootServletInitializer {
    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(EyeApp.class);
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(EyeApp.class, args);
    }
}

